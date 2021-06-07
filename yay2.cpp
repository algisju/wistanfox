/*
 * yay2.cpp
 * 
 * Copyright 2021 geek <geek@KALIBOX>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */



#define _WINSOCK_DEPRECATED_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS

//https://guidedhacking.com/threads/c-winsock-networking-tutorial-introduction.12131/

#pragma comment(lib, "ws2_32.lib")
#include <WinSock2.h>
#include <stdio.h>
#include <stdlib.h>
#include <Windows.h>

#define PORT 80

const char szHost[] = "www.google.com";

int main(const int argc, const char *argv[]) {
    // Init WINSOCK
    WSAData wsaData;
    WORD DllVersion = MAKEWORD(2, 1);
    if (WSAStartup(DllVersion, &wsaData) != 0) {
        fprintf(stderr, "WSAStartup()\n");
        getchar();
        ExitProcess(EXIT_FAILURE);
    }

    // Create socket
    SOCKET sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        fprintf(stderr, "socket()\n");
        getchar();
        ExitProcess(EXIT_FAILURE);
    }

    // Get Server info
    HOSTENT *host = gethostbyname(szHost);
    if(host == nullptr) {
        closesocket(sock);
        fprintf(stderr, "gethostbyname()\n");
        getchar();
        ExitProcess(EXIT_FAILURE);
    }

    // Define server info
    SOCKADDR_IN sin;
    ZeroMemory(&sin, sizeof(sin));
    sin.sin_port = htons(PORT);
    sin.sin_family = AF_INET;
    memcpy(&sin.sin_addr.S_un.S_addr, host->h_addr_list[0], sizeof(sin.sin_addr.S_un.S_addr));

    // Connect to server
    if (connect(sock, (const sockaddr *)&sin, sizeof(sin)) != 0) {
        closesocket(sock);
        fprintf(stderr, "connect()\n");
        getchar();
        ExitProcess(EXIT_FAILURE);
    }
    // Send data to server
    const char szMsg[] = "HEAD / HTTP/1.0\r\n\r\n";
    if (!send(sock, szMsg, strlen(szMsg), 0)) {
        closesocket(sock);
        fprintf(stderr, "send()\n");
        getchar();
        ExitProcess(EXIT_FAILURE);
    }

    // Recieve data back from server
    char szBuffer[4096];
    char szTemp[4096];
    while (recv(sock, szTemp, 4096, 0))
        strcat(szBuffer, szTemp);

    printf("%s\n", szBuffer);

    closesocket(sock);
    getchar();
    ExitProcess(EXIT_SUCCESS);
}


