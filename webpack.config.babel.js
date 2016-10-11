import path from 'path';
import webpack from 'webpack';
import ExtractTextPlugin from 'extract-text-webpack-plugin';

let config = {
  entry: {
    app: path.resolve('app.js'),
    vendor: ['react', 'react-dom', 'react-mdl', 'react-relay', 'react-router', 'react-router-relay']
  },
  output: {
    path: path.resolve('dist'),
    filename: '[name].js',
    publicPath: '/'
  },
  module: {
    loaders: [
      {test: /\.js(x)?$/, loaders: ['react-hot', 'babel'], exclude: /node_modules/}
    ]
  },
  plugins: [
    new webpack.optimize.CommonsChunkPlugin('vendor', 'vendor.js'),
    new webpack.NoErrorsPlugin(),
    new webpack.HotModuleReplacementPlugin(),
    new webpack.DefinePlugin({
      __DEV__: true
    })
  ]
};

export default config;
