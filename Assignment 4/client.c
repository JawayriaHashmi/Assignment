// Client side C/C++ program to demonstrate Socket programming 
#include <stdio.h> 
#include <sys/socket.h> 
#include <stdlib.h> 
#include <netinet/in.h> 
#include <string.h> 
#define PORT 8080 
   
int main() 
{ 
    struct sockaddr_in address; 
    int sock = 0, valread; 
    struct sockaddr_in serv_addr; 
    char *hello = "Hello World"; 
    
    sock = socket(AF_INET, SOCK_STREAM, 0); 
    
    memset(&serv_addr, '0', sizeof(serv_addr)); 
   
    serv_addr.sin_family = AF_INET; 
    serv_addr.sin_port = htons(PORT); 
       
    inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr);  
   
    connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr));
    write(sock , hello , strlen(hello)+1 ); 
    return 0; 
} 

