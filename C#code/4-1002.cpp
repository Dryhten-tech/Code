#include <stdio.h>
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

struct balloons{
    int y;
    string m;
    int d;
}r[100],t;

bool cmp_y(balloons f,balloons e){
    return f.y < e.y;
}

bool cmp_m(balloons f,balloons e){
    if(f.m==e.m){
        return f.y < e.y;
    }
    return f.m<e.m;
}

bool cmp_d(balloons f,balloons e){
    if(f.d == e.d){
        return f.y < e.y;
    }
    return f.d < e.d;
}

int main(){
    int n,c,b,k=1;
    while(scanf("%d%d",&n,&c)!=EOF){
        if(n==0){
            break;
        }
        for(int i = 0;i < n;i ++){
            cin>>r[i].y>>r[i].m>>r[i].d;
        }
        if(c==1){
            sort(r,r+n,cmp_y);
        }else if(c==2){
            sort(r,r+n,cmp_m);
        }else if(c==3){
            sort(r,r+n,cmp_d);
        }
        printf("Case %d:\n",k);
        k++;
        for(int i = 0;i < n;i ++){
            printf("%06d",r[i].y);
            cout<<" "<<r[i].m<<" "<<r[i].d<<endl;
        }
        
    }
    system("pause");
    return 0;
}