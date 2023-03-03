#include<iostream>
#include<fstream>
using namespace std;

const int max_size = 10010;
class Large_Int
{
public:
	int d[max_size] = {0};
	Large_Int(int a[], int n)
	{
		for (int i = 0; i < n; i++)
		{
			d[i] = a[i];
		}
	}
	friend ostream& operator <<(ostream& out, const Large_Int& k);
	Large_Int operator+(const Large_Int& b)
	{
		int count = max_size - 1;
		int temp[1] = {0};
		Large_Int result(temp, 1);
		while (count >= 0)
		{
			result.d[count] += this->d[count] + b.d[count];
			if (result.d[count] >= 10)
			{
				result.d[count] -= 10;
				result.d[count - 1] += 1;
			}
			count--;
		}
		return result;
	}
	Large_Int operator-(const Large_Int& b)
	{
		int count = max_size - 1;
		int temp[1] = { 0 };
		Large_Int result(temp, 1);
		while (count >= 0)
		{
			result.d[count] += (this->d[count] - b.d[count]);
			if (result.d[count] < 0)
			{
				result.d[count] += 10;
				result.d[count - 1] -= 1;
			}
			count--;
		}
		return result;
	}
	Large_Int operator/(const int& b)
	{
		int dividend;
		int remainder = 0;
		int quotient;
		int temp[1] = { 0 };
		Large_Int result(temp, 1);
		for (int i = 0; i < max_size; i++)
		{
			dividend = remainder * 10 + this->d[i];
			quotient = dividend / b;
			remainder = dividend % b;
			result.d[i] = quotient;
		}
		return result;
	}
	int level()
	{
		int level = 0;
		while (true)
		{
			if (this->d[level] != 0) return level;
			level++;
		}
	}
};

ostream& operator <<(ostream& out, const Large_Int& k)
{
	for (int i = 0; i < max_size; i++)
	{
		cout << k.d[i];
	}
	return out;
}

int level_required(Large_Int a, int p)//p counts from 1
{
	while (a.d[p]==9)
	{
		p++;
	}
	return p;
}

Large_Int base_natural()
{
	ofstream f;
	f.open("e.txt");
	int progress = 1;
	int k = 1;
	int test1[1] = { 1 };
	int test2[1] = { 0 };
	Large_Int fac(test1, 1);
	Large_Int result(test1, 1);
	while (true)
	{
		fac = fac / k;
		result = result + fac;
		if (fac.level() >= level_required(result, progress))
		{
			cout <<result.d[progress-1] ;
			f<< result.d[progress - 1];
			progress++;
		}
		k++;
		if (progress == max_size-10 + 1) { f.close(); return result; }
	}
}

int main()
{
	base_natural();
}