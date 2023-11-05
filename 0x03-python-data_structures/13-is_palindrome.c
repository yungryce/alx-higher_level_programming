#include "lists.h"

/**
 * is_palindrome - chesch if the values of a linked list are palindromes
 * @head: pointer to a linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *temp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}

	if (fast)
		slow = slow->next;

	while (prev && slow)
	{
		if (prev->n != slow->n)
			return (0);

		prev = prev->next;
		slow = slow->next;
	}
	return (1);
}
