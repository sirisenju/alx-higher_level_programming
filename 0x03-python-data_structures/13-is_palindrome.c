#include "lists.h"
/**
 * reverse_list - reverse second half of list
 * @head: head of second half
 * Return: void
 */
void reverse_list(listint_t **head)
{
	listint_t *previous, *current, *next;

	previous = NULL;
	current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	*head = previous;
}
/**
 * compare_list - compare each element of list
 * @head1: head first half
 * @head2: head second half
 * Return: 0 if success else 1
 */
int compare_list(listint_t *head1, listint_t *head2)
{
	listint_t *temp1, *temp2;

	temp1 = head1;
	temp2 = head2;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return(0);
		}
	}
	if (temp1 == NULL && temp2 == NULL)
	{
		return (1);
	}
	return (0);
}
/**
 * is_palindrome - check if SLL is palindrome
 * @head: pointer to head of list
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *half, *middle;
	int check;

	slow = fast = prev_slow = *head;
	middle = NULL;
	check = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}
		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}
		half = slow;
		prev_slow->next = NULL;
		reverse_list(&half);
		check = compare_list(*head, half);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = half;
		}
		else
		{
			prev_slow->next = half;
		}
	}
	return (check);
}
