import webpack from 'webpack'
import WebpackDevServer from 'webpack-dev-server'
import webpackConfig from './webpack.config'
import path from 'path'

const relayServer = new WebpackDevServer(webpack(webpackConfig), {
  contentBase: '/build/',
  proxy: {
    '/graphql': `http://127.0.0.1:5000`
  },
  stats: {
    colors: true
  },
  hot: true,
  historyApiFallback: true
});

relayServer.listen(8080, () => console.log('Relay is listening on port 8080.'));
