#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include "hacking.h"

// ユーザが接続するポート番号
#define PORT 7890

int main(void){
    // sockfd上で待ち受ける,new_fdは新たな接続
    int sockfd, new_sockfd;
    // 自らのidアドレス
    struct socksddr_in host_addr,client_addr;
    socklen_t sin_size;
    int recv_length = 1, yes = 1;
    char buffer[1024];

    if ((socket = socket(PF_INET,SOCK_STREAM,0)) == 1){
        fatal("can't create socket.");
    }
    if(setsocket(sockfd,SOL_SOCKET,SO_REUSEADDR,&yes,sizeof(int)== -1)){
        fatal("setting socket to SO_REUSEADDR")
    }
}