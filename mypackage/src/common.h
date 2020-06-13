#ifndef __COMMON__H__
#define __COMMON__H__

#ifdef WIN32
#define EXPORT __declspec(dllexport)
#else 
#define EXPORT 
#endif 

#endif 