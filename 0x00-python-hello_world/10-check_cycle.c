#include "lists.h"

/**
 * check_cycle - function in C that checks if a
 *             singly linked list has a cycle in it
 * @list: list struct
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;

	if (!list || !(list->next))
		return (0);

	while (list && tortoise)
	{
		tortoise = tortoise->next;

		if (tortoise == list)
			return (1);
	}
	return (0);
}

