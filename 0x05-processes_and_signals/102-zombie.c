#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Enters an infinite loop.
 *
 * Return: Always returns 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point
 *
 * Return: 0 if successful otherwie 1.
 */
int main(void)
{
	pid_t pid[5];
	int i;

	for (i = 0; i < 5; i++)
	{
		pid[i] = fork();

		if (pid[i] < 0)
		{
			perror("Fork failed");
			exit(EXIT_FAILURE);
		}

		if (pid[i] == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(EXIT_SUCCESS);
		}
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
