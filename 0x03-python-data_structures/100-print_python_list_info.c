#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints info about a python list
 * @p: PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int size, num;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);
	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (num = 0; num < size; num++)
	{
		item = PyList_GetItem(p, num);
		printf("Element %ld: %s\n", num, Py_TYPE(item)->tp_name);
	}
}
