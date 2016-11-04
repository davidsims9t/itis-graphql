const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const webpack = require('webpack');

const config = {
  devtool: 'eval',
  entry: path.join(__dirname, 'app.js'),
  output: {
    path: path.join(__dirname, 'dist'),
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        include: __dirname,
        use: {
          loader: 'babel',
          options: {
            presets: ["es2015", "stage-0", "react"],
            plugins: ['transform-runtime', path.join(__dirname, '/build/babelRelayPlugin')]
          }
        },
        exclude: /node_modules/
      }
    ]
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.DefinePlugin({
      __DEV__: true
    }),
    new HtmlWebpackPlugin({
      title: 'ITIS',
      cache: false,
      template: path.join(__dirname, 'src/template.ejs')
    })
  ]
};

module.exports = config;
