/* global Maplace */
'use strict';


var maxChapterNumber;
var chaptersTree;
var jsonstr = jsonstr || '[{"id"=>1, "title"=>"The start", "chapter_no"=>1, "parent_id"=>0, "novel_id"=>nil, "created_at"=>Sun, 08 Nov 2015 19:14:01 UTC +00:00, "updated_at"=>Sun, 08 Nov 2015 19:14:01 UTC +00:00, "user_id"=>nil, "abstract"=>nil}]';

function getData() {
  return JSON.parse(jsonstr.replace(/=>/g, ':').replace(/nil/g, '0'));
}

function getChapters(data, chapterNumber, parentId) {
  return data.filter(function(item){
    return ((parentId === 0 || item.parent_id === parentId) && item.chapter_no === chapterNumber);
  });
}

function getMaxChapter(data) {
  return data.reduce(function(a, b){
    return a.chapter_no >= b.chapter_no? a : b;
  }, {ch:0});
}

function _buildTreeLevels(data) {
  
  var max = getMaxChapter(data).chapter_no;
  maxChapterNumber = max;
  var resultTree = new Array(max);
  for (var i = 0; i < max; i++) {
    resultTree[i] = getChapters(data, i + 1, 0);
  }
  return resultTree;
}

function chapterToSlide(chapter){
  return '<div class="slide" id="' + chapter.id +'" data-parent="' + chapter.parent_id + '">'
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
    return chapter.parent_id === chapter2.parent_id
  });
}

function getChapterChildren(chapters, chapterid) {
  return chapters.filter(function(chapter2) {
    return chapter.id === chapter2.parent_id
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