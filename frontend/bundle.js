/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var canvas = document.querySelector('canvas');
var ctx = canvas.getContext("2d");

var clickX = [];
var clickY = [];
var clickDrag = [];
var drawing;

function clearCanvas() {
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
}

function addClick(x, y, dragging) {
    clickX.push(x);
    clickY.push(y);
    clickDrag.push(dragging);
}

function redraw() {
    clearCanvas();
    ctx.strokeStyle = "#000000";
    ctx.lineJoin = "round";
    ctx.lineWidth = 5;

    clickX.forEach(function (click, i) {
        ctx.beginPath();
        if (clickDrag[i] && i) {
            ctx.moveTo(clickX[i - 1], clickY[i - 1]);
        } else {
            ctx.moveTo(clickX[i] - 1, clickY[i]);
        }
        ctx.lineTo(clickX[i], clickY[i]);
        ctx.closePath();
        ctx.stroke();
    });
}

canvas.addEventListener("mousedown", function (e) {
    var mouseX = e.pageX - this.offsetLeft - this.offsetParent.offsetLeft;
    var mouseY = e.pageY - this.offsetTop - this.offsetParent.offsetTop;
    drawing = true;
    addClick(mouseX, mouseY);
    redraw();
});

canvas.addEventListener("mousemove", function (e) {
    if (drawing) {
        var mouseX = e.pageX - this.offsetLeft - this.offsetParent.offsetLeft;
        var mouseY = e.pageY - this.offsetTop - this.offsetParent.offsetTop;
        addClick(mouseX, mouseY);
        redraw();
    }
});

canvas.addEventListener("mouseup", function (e) {
    drawing = false;
});

canvas.addEventListener("mouseleave", function (e) {
    drawing = false;
});

document.querySelector('#clear-button').addEventListener("click", function (e) {
    clearCanvas();
    clickX = [];
    clickY = [];
    clickDrag = [];
});

function simplifyArray(imageArr) {
    var simpleArr = imageArr.filter(function (value, index) {
        return (index + 1) % 4 == 0;
    });
    simpleArr = simpleArr.map(function (value) {
        return value / 255;
    });
    return Array.from(simpleArr);
}

document.querySelector('#submit-button').addEventListener("click", function (e) {
    var imageData = ctx.getImageData(0, 0, ctx.canvas.width, ctx.canvas.height);
    console.log(imageData);
    console.log(simplifyArray(imageData.data));
});

/***/ })
/******/ ]);