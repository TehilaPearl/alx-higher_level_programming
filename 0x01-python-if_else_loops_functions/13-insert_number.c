#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
* insert_node - function
* @head: beginning of list
* @number: number to insert
*
* Description: Function to insert a number to a sorted list
* Return: address of new node, or NULL if Fail
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	if (*head == NULL)
	{
		newNode = (*head)->next;
		newNode->next = NULL;
		(*head) = newNode;
		return (newNode);
	}
	newNode->n = number;
	newNode->next = (*head)->next;
	newNode->next = (*head);
	(*head) = newNode;
	return (newNode);
}
