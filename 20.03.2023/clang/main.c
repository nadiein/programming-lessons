// Given a string with the weights of FFC members in normal order,
// give this string ordered by "weights" of these numbers


#include <stdio.h>
#include <stdlib.h>
#include <string.h>


// TODO: Write unit tests!
// Function to calculate the "weight" of a given number
int weight(char* num) {
    int w = 0;

    for (int i = 0; num[i] != '\0'; i++) {
        w += num[i] - '0';
    }

    return w;
}

// Custom comparison function for qsort to sort numbers by weight
int cmp(const void* a, const void* b) {
    char* numa = *(char**)a;
    char* numb = *(char**)b;
    int wa = weight(numa);
    int wb = weight(numb);

    if (wa != wb) {
        return wa - wb;
    } else {
        return strcmp(numa, numb);
    }
}

// Main function to order the given string of weights
char* orderWeight(const char* s) {
    // Make a copy of the input string to avoid modifying the original
    char* s_copy = strdup(s);

    if (s_copy == NULL) {
        return NULL;
    }
    
    // Split the string into tokens based on whitespace
    char* tok = strtok(s_copy, " \t\n\r");
    char* nums[1000];
    int n = 0;

    while (tok != NULL) {
        nums[n++] = tok;
        tok = strtok(NULL, " \t\n\r");
    }

    // Sort the numbers using custom comparison function
    qsort(nums, n, sizeof(char*), cmp);

    // Concatenate the sorted numbers into a single string
    char* result = (char*)malloc(strlen(s) + 1);

    if (result == NULL) {
        free(s_copy);

        return NULL;
    }

    result[0] = '\0';

    for (int i = 0; i < n; i++) {
        strcat(result, nums[i]);

        if (i < n - 1) {
            strcat(result, " ");
        }
    }

    free(s_copy);

    return result;
}