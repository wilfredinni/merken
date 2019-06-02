("use strict");

var gulp = require("gulp");
var sass = require("gulp-sass");
var postcss = require("gulp-postcss");
var autoprefixer = require("autoprefixer");
var cssnano = require("cssnano");
var sourcemaps = require("gulp-sourcemaps");
var uglify = require("gulp-uglify-es").default;
var rename = require("gulp-rename");

sass.compiler = require('node-sass');

var paths = {
  styles: {
    src: "./static/merken/dev/sass/*.scss",
    dest: "./static/merken/css"
  },
  js: {
    src: "./static/merken/dev/js/*.js",
    dest: "./static/merken/js"
  }
};

function style() {
  return gulp
    .src(paths.styles.src)
    .pipe(sourcemaps.init())
    .pipe(sass())
    .on("error", sass.logError)
    .pipe(rename({ suffix: ".min" }))
    .pipe(postcss([autoprefixer(), cssnano()]))
    .pipe(sourcemaps.write())
    .pipe(gulp.dest(paths.styles.dest));
}

function compressJs() {
  return gulp
    .src(paths.js.src)
    .pipe(rename({ suffix: ".min" }))
    .pipe(sourcemaps.init())
    .pipe(uglify())
    .pipe(sourcemaps.write())
    .pipe(gulp.dest(paths.js.dest));
}

function watch() {
  gulp.watch(paths.styles.src, style);
  gulp.watch(paths.js.src, compressJs);
}

exports.style = style;
exports.compressJs = compressJs;
exports.watch = watch;
