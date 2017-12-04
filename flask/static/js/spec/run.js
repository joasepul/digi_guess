import Jasmine from 'jasmine';

const jasmine = new Jasmine();
jasmine.loadConfigFile('./js/spec/support/jasmine.json');
jasmine.execute();