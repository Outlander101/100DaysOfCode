#include<iostream>

using namespace std;
template<class T>

class Array
{
private:
    T *A;
    int size;
    int length;

public:
    Array() 
    {
        size = 10;
        A = new T[size];
        length = 0;
    }

    Array(int sz)
    {
        size = sz;
        A = new int[size];
        length = 0;
    }

    ~Array()
    {
        delete []A;
    }

    void Display();
    void Insert(int index, T x);
    T Delete(int index);
};

template<class T>
void Array<T>::Display()
{
    for(int i = 0; i < length; i++)
        cout << A[i] << " ";
    cout << endl;
}

template<class T>
void Array<T>::Insert(int index, T x)
{
    if(index>=0 && index<=length && index<size)
    {
        for(int i = length - 1; i >= index; i--)
            A[i+1] = A[i];
        A[index] = x;
        length++;
    }
}

template<class T>
T Array<T>::Delete(int index)
{
    T x;
    if(index>=0 && index<length)
    {
        x = A[index];
        for(int i = index; i < length - 1; i++)
            A[i] = A[i+1];
        length--;
    }
    return x;
}

int main() 
{
    cout << "Enter the size of the array: ";
    int arr_size;
    if (!(std::cin >> arr_size)) {
        cout << "Not a valid integer!" << std::endl;
        cin.clear(); // Reset error state
        cin.ignore(1000, '\n'); // Clear the buffer
    }
    Array<int> arr(arr_size);
    cout << "Enter the array values: \n";
    int elements;
    for(int i = 0; i < arr_size; i++)
    {
        cin >> elements;
        arr.Insert(i, elements);
    }
    arr.Display();
    arr.Delete(0);
    arr.Display();
    return 0;
}