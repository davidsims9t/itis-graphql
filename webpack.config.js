const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const webpack = require('webpack');

const config = {
  devtool: 'cheap-module-eval-source-map',
  entry: path.join(__dirname, 'app.js'),
  output: {
    path: path.join(__dirname, 'dist'),
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        loader: 'babel',
        include: __dirname,
        options: {
          presets: ["es2015", "stage-0", 'react'],
          plugins: ['transform-runtime']
        },
        exclude: /node_modules/
      }
    ]
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.DefinePlugin({
      "process.env.NODE_ENV": '"development"',
      __DEV__: true
    }),
    new HtmlWebpackPlugin({
      title: 'ITIS',
      cache: true
    })
  ]
};

module.exports = config;
