#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main()
{
    int n;
    printf("Enter the size of the array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the elements of the array: ");
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    int fd[2];
    if (pipe(fd) == -1)
    {
        fprintf(stderr, "Pipe failed");
        return 1;
    }
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        pid_t pid = fork();
        if (pid < 0)
        {
            printf("Fork failed\n");
            return 1;
        }
        else if (pid == 0)
        { // child process
            sum += arr[i];
            write(fd[1], &sum, sizeof(sum)); // write the new sum to the pipe
            printf("Partial sum in child process %d: %d\n", i, sum);
            return 0; // end child process
        }
        else
        {                                   // parent process
            wait(NULL);                     // wait for child process to finish
            read(fd[0], &sum, sizeof(sum)); // read the new sum from the pipe
        }
    }
    return 0;
}