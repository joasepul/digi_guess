import Jasmine from 'jasmine';

let jasmine = new Jasmine();
jasmine.loadConfigFile('./js/spec/support/jasmine.json');
jasmine.execute();