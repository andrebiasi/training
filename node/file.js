var fs = require('fs')
  , sys = require('util');

var my_text = ""

fs.readFile('test-input.txt', function(report) {
  my_text = report;
  sys.puts("My test file: "+report);
});

fs.writeFile('test-output.txt', my_text, function() {
  sys.puts("blablabla");
});
