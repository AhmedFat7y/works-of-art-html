/* global Maplace */
'use strict';
function getData() {
  return [
    {
      id:1, 
      ch:1, 
      pid:0, 
      title: 'hello world-1'
    },
    {
      id:2, 
      ch:2, 
      pid:1, 
      title: 'hello world-2'
    },
    {
      id:3, 
      ch:3, 
      pid:2, 
      title: 'hello world-3'
    },
    {
      id:4, 
      ch:3, 
      pid:2, 
      title: 'hello world-4'
    },
    {
      id:5, 
      ch:2, 
      pid:1, 
      title: 'hello world-5'
    },
    {
      id:6,
      ch:3,
      pid:5, 
      title: 'hello world-6'
    },
  ];
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

var chaptersTree = buildChapterSlides();