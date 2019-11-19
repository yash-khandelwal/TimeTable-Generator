var v1 = Module['vec']();

var v2 = Module['vec']();

var v3 = Module['vec']();

var v4 = Module['vec']();
var v6 = Module['vec']();

var v4 = Module['vec_int']();

var v5 = Module['vec_int']();


for(var i=0; i < course.length; i++ ){
    v1.push_back(course[i][0]);
    v2.push_back(course[i][1]);
    v6.push_back(course[i][2]);
    v3.push_back(course[i][3]);
    v4.push_back(parseInt(course[i][4]));
    v5.push_back(parseInt(course[i][5]));}

var getCourse = Module['getCourse'](v1, v2, v3, v4, v5);
var getTeacher = Module['getTeacher'](v2, v6);
