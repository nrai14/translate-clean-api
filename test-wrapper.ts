import axios from "axios";
import * as ExcelJS from "exceljs";

const TRANSLATION_SERVICE_URL = "http://127.0.0.1:5000/translate";
const WORDS_FILE_PATH = "data/wordsToTranslate.xlsx";
const RESULTS_FILE_PATH = "results/translatedWords.xlsx";
const TARGET_LANGUAGES = ["es", "fr", "de"];

interface TranslateRequestBody {
  words: string[];
  targetLanguage: string;
}

interface TranslateResponseBody {
  words: TranslatedWord[];
  targetLanguage: string;
}

interface TranslatedWord {
  originalWord: string;
  translatedWord: string;
}

async function readWordsFromSpreadsheet(filePath: string): Promise<string[]> {
  console.log("Reading words from spreadsheet:", filePath);
  const workbook = new ExcelJS.Workbook();
  await workbook.xlsx.readFile(filePath);
  console.log("Spreadsheet read successfully");
  const worksheet = workbook.getWorksheet(1)!;
  const words: string[] = [];
  worksheet.eachRow((row) => {
    // Assuming words are in the first column
    words.push(row.getCell(1).text);
  });
  console.log("Words extracted from spreadsheet:", words);
  return words;
}

async function translateWords(
    words: string[],
    targetLanguages: string[],
    resultsFilePath: string
  ): Promise<void> {
    console.log("Starting translation process with words:", words, " and target languages:", targetLanguages);
    const translationResponses: TranslateResponseBody[] = [];
  
    for (const targetLanguage of targetLanguages) {
      const requestBody: TranslateRequestBody = {
        words: words,
        targetLanguage: targetLanguage,
      };
  
      console.log("Payload sent to /translate:", requestBody);
  
      try {
        const response = await axios.post(TRANSLATION_SERVICE_URL, requestBody);
  
        // Safely parse and validate response.data
        if (response.data) {
          const responseBody = response.data as TranslateResponseBody;
          if (Array.isArray(responseBody.words) && typeof responseBody.targetLanguage === 'string') {
            translationResponses.push(responseBody);
          } else {
            console.error('Unexpected response structure:', response.data);
          }
        }
      } catch (error) {
        console.error(
          `Error calling the translate endpoint ${TRANSLATION_SERVICE_URL} with target language ${targetLanguage}:`,
          error
        );
      }
    }
  
    console.log("Saving translations to spreadsheet:", translationResponses);
    await saveWordsToSpreadsheet(translationResponses, resultsFilePath);
  }
  

async function saveWordsToSpreadsheet(
  translationResponses: TranslateResponseBody[],
  filePath: string
): Promise<void> {
  console.log("Creating workbook for translated words:", filePath);
  const workbook = new ExcelJS.Workbook();

  for (const translationResponse of translationResponses) {
    console.log("Processing translation response for target language:", translationResponse.targetLanguage);
    const worksheet = workbook.addWorksheet(
      `${translationResponse.targetLanguage} translations`
    );

    translationResponse.words.forEach((word) => {
      worksheet.addRow([word.originalWord, word.translatedWord]);
    });
  }

  await workbook.xlsx.writeFile(filePath);
  console.log(`Translated words saved successfully to ${filePath}`);
}

// Example usage
readWordsFromSpreadsheet(WORDS_FILE_PATH)
  .then((words) => translateWords(words, TARGET_LANGUAGES, RESULTS_FILE_PATH))
  .catch((error) => console.error("Error in process", error));
