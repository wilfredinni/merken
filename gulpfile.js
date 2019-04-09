("use strict");

var gulp = require("gulp");
var sass = require("gulp-sass");

var paths = {
  styles: {
    src: "./src/default_template_dev/sass/*.scss",
    dest: "./src/static_in_env/css"
  }
};

function style() {
  return gulp
    .src(paths.styles.src)
    .pipe(sass())
    .on("error", sass.logError)
    .pipe(gulp.dest(paths.styles.dest));
}

function watch() {
  gulp.watch(paths.styles.src, style);
}

exports.style = style;
exports.watch = watch;
