#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    // Print header for browser
    printf("Content-Type: text/html\n\n");
    
    char *data = getenv("QUERY_STRING");
    
    printf("<html><head><style>body{background:#0f172a;color:white;text-align:center;padding-top:100px;font-family:sans-serif;}</style></head><body>");

    if (data != NULL && strlen(data) > 0) {
        // Save vote to file
        FILE *f = fopen("votes.dat", "a");
        if (f != NULL) {
            fprintf(f, "%s\n", data); // Saves "candidate=Alice_Johnson"
            fclose(f);
            printf("<h1>✅ Vote Success</h1><p>Your selection has been encrypted and stored.</p>");
        }
    } else {
        printf("<h1>❌ Error</h1><p>No selection detected.</p>");
    }

    printf("<br><a href='/index.html' style='color:#6366f1;text-decoration:none;'>Return to Dashboard</a></body></html>");
    return 0;
}