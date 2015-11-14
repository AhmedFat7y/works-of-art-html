/* global Maplace */
'use strict';

var maxChapterNumber;
var chaptersTree;

function getData() {
  var jsonstr = '[{"ch": 1, "id": 1, "title": "hello-1", "pid": 0},{"ch": 2, "id": 2, "title": "hello-2", "pid": 1},{"ch": 2, "id": 3, "title": "hello-3", "pid": 1},{"ch": 2, "id": 4, "title": "hello-4", "pid": 1},{"ch": 2, "id": 5, "title": "hello-5", "pid": 1},{"ch": 3, "id": 6, "title": "hello-6", "pid": 2},{"ch": 3, "id": 7, "title": "hello-7", "pid": 2},{"ch": 3, "id": 8, "title": "hello-8", "pid": 2},{"ch": 3, "id": 9, "title": "hello-9", "pid": 2},{"ch": 3, "id": 10, "title": "hello-10", "pid": 3},{"ch": 3, "id": 11, "title": "hello-11", "pid": 3},{"ch": 3, "id": 12, "title": "hello-12", "pid": 3},{"ch": 3, "id": 13, "title": "hello-13", "pid": 3},{"ch": 3, "id": 14, "title": "hello-14", "pid": 4},{"ch": 3, "id": 15, "title": "hello-15", "pid": 4},{"ch": 3, "id": 16, "title": "hello-16", "pid": 4},{"ch": 3, "id": 17, "title": "hello-17", "pid": 4},{"ch": 3, "id": 18, "title": "hello-18", "pid": 5},{"ch": 3, "id": 19, "title": "hello-19", "pid": 5},{"ch": 3, "id": 20, "title": "hello-20", "pid": 5},{"ch": 3, "id": 21, "title": "hello-21", "pid": 5},{"ch": 4, "id": 22, "title": "hello-22", "pid": 6},{"ch": 4, "id": 23, "title": "hello-23", "pid": 6},{"ch": 4, "id": 24, "title": "hello-24", "pid": 6},{"ch": 4, "id": 25, "title": "hello-25", "pid": 6},{"ch": 4, "id": 26, "title": "hello-26", "pid": 7},{"ch": 4, "id": 27, "title": "hello-27", "pid": 7},{"ch": 4, "id": 28, "title": "hello-28", "pid": 7},{"ch": 4, "id": 29, "title": "hello-29", "pid": 7},{"ch": 4, "id": 30, "title": "hello-30", "pid": 8},{"ch": 4, "id": 31, "title": "hello-31", "pid": 8},{"ch": 4, "id": 32, "title": "hello-32", "pid": 8},{"ch": 4, "id": 33, "title": "hello-33", "pid": 8},{"ch": 4, "id": 34, "title": "hello-34", "pid": 9},{"ch": 4, "id": 35, "title": "hello-35", "pid": 9},{"ch": 4, "id": 36, "title": "hello-36", "pid": 10},{"ch": 4, "id": 37, "title": "hello-37", "pid": 10},{"ch": 4, "id": 38, "title": "hello-38", "pid": 11},{"ch": 4, "id": 39, "title": "hello-39", "pid": 11},{"ch": 4, "id": 40, "title": "hello-40", "pid": 11},{"ch": 4, "id": 41, "title": "hello-41", "pid": 12},{"ch": 4, "id": 42, "title": "hello-42", "pid": 12},{"ch": 4, "id": 43, "title": "hello-43", "pid": 12},{"ch": 4, "id": 44, "title": "hello-44", "pid": 12},{"ch": 4, "id": 45, "title": "hello-45", "pid": 12},{"ch": 4, "id": 46, "title": "hello-46", "pid": 13},{"ch": 4, "id": 47, "title": "hello-47", "pid": 13},{"ch": 4, "id": 48, "title": "hello-48", "pid": 14},{"ch": 4, "id": 49, "title": "hello-49", "pid": 14},{"ch": 4, "id": 50, "title": "hello-50", "pid": 15},{"ch": 4, "id": 51, "title": "hello-51", "pid": 15},{"ch": 4, "id": 52, "title": "hello-52", "pid": 15}]';
  return JSON.parse(jsonstr)
}

function getChapters(data, chapterNumber, parentId) {
  return data.filter(function(item){
    return ((parentId === 0 || item.pid === parentId) && item.ch === chapterNumber);
  });
}

function getMaxChapter(data) {
  return data.reduce(function(a, b){
    return a.ch >= b.ch? a : b;
  }, {ch:0});
}

function _buildTreeLevels(data) {
  
  var max = getMaxChapter(data).ch;
  maxChapterNumber = max;
  var resultTree = new Array(max);
  for (var i = 0; i < max; i++) {
    resultTree[i] = getChapters(data, i + 1, 0);
  }
  return resultTree;
}

function chapterToSlide(chapter){
  return '<div class="slide" id="' + chapter.id +'" data-parent="' + chapter.pid + '">'
        +'<div class="slide-content">'
        +'<h4>' + chapter.title + '</h4>'
        +'</div>'
        +'</div>';
}


function buildChapterSlides() {
  var data = getData();
  var chaptersTree = _buildTreeLevels(data);
  return chaptersTree.map(function(level) {
    return level.map(function(chapter) {
      chapter.html = chapterToSlide(chapter);
      return chapter;
    });
  });

}

chaptersTree = buildChapterSlides();


function getChapterSiblings(chapters, chapter) {
  return chapters.filter(function(chapter2) {
    return chapter.pid == chapter2.pid
  });
}

function getChapterChildren(chapters, chapterid) {
  return chapters.filter(function(chapter2) {
    return chapter.id == chapter2.pid
  });
}

function replaceSlides(slider, chapters) {
  clearSlick(slider);
  chapters.forEach(function(chapter, index, array){
    slider.slick('slickAdd', chapter.html);
  });
}

function clearSlick(slider) {
  while (slider.slick('slickRemove', 0)) {}
}