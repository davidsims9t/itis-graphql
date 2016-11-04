var fs = require('fs');
var path = require('path');
var schema = path.join(__dirname, '../data/schema.json');

fs.access(schema, fs.F_OK, function (err) {
  if (!err) module.exports = require('babel-relay-plugin')(require(schema));
});
