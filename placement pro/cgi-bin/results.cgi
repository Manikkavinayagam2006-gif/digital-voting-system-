#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    printf("Content-Type: text/html\n\n");
    
    int alice = 0, bob = 0;
    char buffer[100];
    FILE *f = fopen("votes.dat", "r");

    if (f != NULL) {
        while (fgets(buffer, sizeof(buffer), f)) {
            if (strstr(buffer, "Alice")) alice++;
            if (strstr(buffer, "Bob")) bob++;
        }
        fclose(f);
    }

    printf("<html><head><style>body{background:#0f172a;color:white;font-family:sans-serif;display:flex;justify-content:center;padding-top:50px;}</style></head><body>");
    printf("<div style='background:#1e293b;padding:40px;border-radius:20px;width:300px;text-align:center;'>");
    printf("<h2>Live Results</h2>");
    printf("<p>Alice Johnson: <b>%d</b></p>", alice);
    printf("<p>Bob Smith: <b>%d</b></p>", bob);
    printf("<hr><a href='/index.html' style='color:#6366f1;'>Back</a></div></body></html>");
    
    return 0;
}