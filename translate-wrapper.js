"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype);
    return g.next = verb(0), g["throw"] = verb(1), g["return"] = verb(2), typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
Object.defineProperty(exports, "__esModule", { value: true });
var axios_1 = require("axios");
var ExcelJS = require("exceljs");
var TRANSLATION_SERVICE_URL = "http://127.0.0.1:5000/translate";
var WORDS_FILE_PATH = "data/wordsToTranslate.xlsx";
var RESULTS_FILE_PATH = "results/translatedWords.xlsx";
var TARGET_LANGUAGES = ["es", "fr", "de"];
function readWordsFromSpreadsheet(filePath) {
    return __awaiter(this, void 0, void 0, function () {
        var workbook, worksheet, words;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    workbook = new ExcelJS.Workbook();
                    return [4 /*yield*/, workbook.xlsx.readFile(filePath)];
                case 1:
                    _a.sent();
                    worksheet = workbook.getWorksheet(1);
                    words = [];
                    worksheet.eachRow(function (row) {
                        // Assuming words are in the first column
                        words.push(row.getCell(1).text);
                    });
                    return [2 /*return*/, words];
            }
        });
    });
}
function translateWords(words, targetLanguages, resultsFilePath) {
    return __awaiter(this, void 0, void 0, function () {
        var translationResponses, _i, targetLanguages_1, targetLanguage, requestBody, response, error_1;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    translationResponses = [];
                    _i = 0, targetLanguages_1 = targetLanguages;
                    _a.label = 1;
                case 1:
                    if (!(_i < targetLanguages_1.length)) return [3 /*break*/, 6];
                    targetLanguage = targetLanguages_1[_i];
                    requestBody = {
                        words: words,
                        targetLanguage: targetLanguage,
                    };
                    _a.label = 2;
                case 2:
                    _a.trys.push([2, 4, , 5]);
                    return [4 /*yield*/, axios_1.default.post(TRANSLATION_SERVICE_URL, requestBody)];
                case 3:
                    response = _a.sent();
                    translationResponses.push(response.data);
                    return [3 /*break*/, 5];
                case 4:
                    error_1 = _a.sent();
                    console.error("Error calling the translate endpoint ".concat(TRANSLATION_SERVICE_URL, " with target language ").concat(targetLanguage, ":"), error_1);
                    return [3 /*break*/, 5];
                case 5:
                    _i++;
                    return [3 /*break*/, 1];
                case 6:
                    saveWordsToSpreadsheet(translationResponses, resultsFilePath);
                    return [2 /*return*/];
            }
        });
    });
}
function saveWordsToSpreadsheet(translationResponses, filePath) {
    return __awaiter(this, void 0, void 0, function () {
        var workbook, _loop_1, _i, translationResponses_1, translationResponse;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    workbook = new ExcelJS.Workbook();
                    _loop_1 = function (translationResponse) {
                        var worksheet = workbook.addWorksheet("".concat(translationResponse.targetLanguage, " translations"));
                        translationResponse.words.forEach(function (word) {
                            worksheet.addRow([word.originalWord, word.translatedWord]);
                        });
                    };
                    for (_i = 0, translationResponses_1 = translationResponses; _i < translationResponses_1.length; _i++) {
                        translationResponse = translationResponses_1[_i];
                        _loop_1(translationResponse);
                    }
                    return [4 /*yield*/, workbook.xlsx.writeFile(filePath)];
                case 1:
                    _a.sent();
                    console.log("Translated words saved to ".concat(filePath));
                    return [2 /*return*/];
            }
        });
    });
}
// Example usage
readWordsFromSpreadsheet(WORDS_FILE_PATH)
    .then(function (words) { return translateWords(words, TARGET_LANGUAGES, RESULTS_FILE_PATH); })
    .catch(function (error) { return console.error(error); });
