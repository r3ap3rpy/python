%module example
%{
extern double my_variable;
extern int fact(int n);
extern int modulo(int x, int y);
extern char *get_time();
%}

extern double my_variable;
extern int fact(int n);
extern int modulo(int x, int y);
extern char *get_time();
