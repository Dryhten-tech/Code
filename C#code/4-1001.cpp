#include <stdio.h>
#include <iostream>
#include<math.h>
#include<stdlib.h>
#include<time.h>
#include<string>
#include<cstdio>
#include<cstdlib>
#include <bits/stdc++.h>

using namespace std;

struct balloons{
    char t[100];
    int d;
}r[100];

int main(){
    int n,m,u;
    char a[100];
    char l[100];
    while(scanf("%d",&n)!=EOF){
        for(int i = 0;i < n;i ++){
            scanf("%d",&m);
            for(int j = 0;j < m;j ++){
                scanf("%s %d",r[j].t,&r[j].d);
            }
            for(int j = 0;j < m-1;j ++){
                for(int k = j + 1;k < m;k ++){
                    if(r[j].d < r[k].d){
                        u = r[j].d;
                        strcpy(l,r[j].t);
                        r[j].d = r[k].d;
                        strcpy(r[j].t,r[k].t);
                        r[k].d = u; 
                        strcpy(r[k].t,l);
                    }
                }
            }
            for(int j = 0;j < m-1;j ++){
                printf("%s ",r[j].t);
            }
            printf("%s\n",r[m-1].t);
            
        }
    }
    system("pause");
    return 0;
}