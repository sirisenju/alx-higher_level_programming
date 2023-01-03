#include "lists.h"
/**
 * check_cycle - check if linked list has a loop
 * @list: first node
 * Return: 1 if linked list has loop 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *head1, *head2;

	head1 = head2 = list;

	if (list == NULL)
		return (0);

	while (head1 && head2 && head2->next)
	{
		head1 = head1->next;
		head2 = head2->next->next;

		if (head1 == head2)
		{
			return (1);
		}
	}
	return (0);
}
