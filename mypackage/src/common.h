#ifndef __COMMON__H__
#define __COMMON__H__

// EXPORT is required on windows so that Python can see the exported function in .dll file
#ifdef WIN32
#define EXPORT __declspec(dllexport)
#else 
#define EXPORT 
#endif 

#endif 