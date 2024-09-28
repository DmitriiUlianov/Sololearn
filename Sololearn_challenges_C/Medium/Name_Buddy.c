/* You are grouped into groups for a project, and you are supposed to come up with as many famous scientists who have the same first letter of their name as you as possible.  
Will you have to come up with the answers on your own, or is there somebody in your group that you can work with? 
 
Task:  
Determine if anyone in your group has the same first letter of their name as you. 
 
Input Format:  
A string of your group members' names separated by spaces, and then a string of your name. 
 
Output Format:  
A string that says 'Compare notes' if you have a name buddy, or 'No such luck' if you have to work on this alone. 
 
Sample Input:  
Becky Joan Fred Trey 
Brad 
 
Sample Output:  
Compare notes

Explanation:  
Congratulations! You have a name buddy since Brad and Becky both start with a 'B'. You can work together. */

#include <stdio.h>
#include <string.h>

int main() {

    const int buffer=256;
    char names[buffer];
    fgets(names, buffer, stdin);
    char myName[buffer];
    scanf("%s", &myName);
    
    for(char *token=strtok(names," "); token != NULL; token=strtok(NULL," ")){
        if(token[0] == myName[0]){
            printf("Compare notes");
            return 0;
        }
    }
    printf("No such luck");
    return 0;
}
