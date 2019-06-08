const BundleTracker = require("webpack-bundle-tracker");
require("dotenv").config();
let host = process.env.ALLOWED_HOSTS

const pages = {
  vue_dashboard: {
    entry: "./src/main.js",
    chunks: ["chunk-vendors"]
  }
  // 'vue_app_02': {
  //     entry: './src/otherMain.js',
  //     chunks: ['chunk-vendors']
  // },
};

module.exports = {
  pages: pages,
  filenameHashing: false,
  productionSourceMap: true,
  publicPath:
    process.env.NODE_ENV === "production"
      ? `http://${host}/static/dashboard/`
      : "http://127.0.0.1:8080/",
  outputDir: "../static/dashboard/",

  chainWebpack: config => {
    config.optimization.splitChunks({
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: "chunk-vendors",
          chunks: "all",
          priority: 1
        }
      }
    });

    Object.keys(pages).forEach(page => {
      config.plugins.delete(`html-${page}`);
      config.plugins.delete(`preload-${page}`);
      config.plugins.delete(`prefetch-${page}`);
    });

    config
      .plugin("BundleTracker")
      .use(BundleTracker, [{ filename: "../dashboard/webpack-stats.json" }]);

    // config.resolve.alias.set("__STATIC__", "static");

    config.devServer
      .public("http://localhost:8080")
      .host("localhost")
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .headers({ "Access-Control-Allow-Origin": ["*"] });
  }
};
