/*
 * Hashing.cpp
 *
 *  Created on: Jul 12, 2022
 *      Author: yannik
 */


#include <vector>
#include <string>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include "Linkedlist.h"

class Customer{
 public:
	string lastname;
	string firstname;
	string id;

  Customer()
    :lastname("")
    ,firstname("")
    ,id("")
  {}

  Customer(string _lastname, string _firstname, string _id)
    :lastname(_lastname)
    ,firstname(_firstname)
    ,id(_id)
  {}

  bool operator==(const Customer &other) const {
    return lastname == lastname && firstname == firstname && id == id;
  }

  friend ostream& operator<<(ostream &os, const Customer &customer);
};

ostream& operator<<(ostream &os, const Customer &customer) {
  os << customer.lastname << ' ' << customer.firstname << ' ' << customer.id << '\n';
  return os;
}

const unsigned int TABLE_SIZE = 400;
//static int maximum = TABLE_SIZE;

// basic modulo division
int hashFunc(string k) {
  int ret = 0;
  for (char c : k) {
    ret += c;
	//ret = (ret << 5) + ret + c;
    ret %= TABLE_SIZE;
  }
  return abs(ret);
}

// mid square
int hashFunc2(string k) {
  int ret = 0;
  int res;
  for (char c : k) {
    ret += c;
  }
  return ((ret*ret)/10) % TABLE_SIZE;
}

// digit folding
int hashFunc3(string k) {
  long ret = 0, mul = 1;
  for (int i = 0; i < k.length(); i++) {
    mul = (i % 4 == 0) ? 1 : mul * 256;
    ret += k.at(i) * mul;
  }
  return (int)(abs(ret) % TABLE_SIZE);
}

// multiplication hashing
int hashFunc4(string k) {
  int ret = 0;
  for (char c : k) {
    ret += c;
  }
  float decimal = (abs(ret)*.5436)-floor(abs(ret)*.5436);
  return floor(decimal*TABLE_SIZE);
}

class HashTable {
 private:
	int collisions = 0;
    vector<DList<Customer> > table;

 public:
	HashTable(int s = 1) {
    table.resize(s);
	}

	int size() {
		return table.size();
	}

	int getcollisions() {
		return collisions;
	}

	Customer get(Customer customer) {
		int hash = hashFunc(customer.id);
		return table[hash].Search(customer)->data;
	}

	Customer get2(Customer customer) {
		int hash = hashFunc2(customer.id);
		return table[hash].Search(customer)->data;
	}

	Customer get3(Customer customer) {
		int hash = hashFunc3(customer.id);
		return table[hash].Search(customer)->data;
	}

	Customer get4(Customer customer) {
		int hash = hashFunc4(customer.id);
		return table[hash].Search(customer)->data;
	}

	DList<Customer> get(int index) {
		return table[index];
	}

	void set(Customer customer) {
		int hash = hashFunc(customer.id);
		if (!(table[hash].IsEmpty()) ) {
			collisions++;
		}
		table[hash].Append(customer);
	}

	void set2(Customer customer) {
			int hash = hashFunc2(customer.id);
			if (!(table[hash].IsEmpty()) ) {
				collisions++;
			}
			table[hash].Append(customer);
		}

	void set3(Customer customer) {
			int hash = hashFunc3(customer.id);
			if (!(table[hash].IsEmpty()) ) {
				collisions++;
			}
			table[hash].Append(customer);
		}

	void set4(Customer customer) {
			int hash = hashFunc4(customer.id);
			if (!(table[hash].IsEmpty()) ) {
				collisions++;
			}
			table[hash].Append(customer);
		}

	DList<Customer> operator [] (int index) {
		return get(index);
	}
};

int main() {
  string line;
  HashTable htable(TABLE_SIZE);
  HashTable htable2(TABLE_SIZE);
  HashTable htable3(TABLE_SIZE);
  HashTable htable4(TABLE_SIZE);

  ifstream fin("Customer.csv");
  while (getline(fin, line)) {
    string token;
    vector<string> tokens;
    for (char c : line) {
      if (c == ',') {
        tokens.push_back(token);
        token = "";
        continue;
      }
      token += c;
    }
    token.pop_back();
    tokens.push_back(token);
    cout << "Current data is " << tokens[0] << ' ' <<
    		tokens[1] << ' ' << tokens[2] << " with hash = " <<
			hashFunc(tokens[2]) << " and the bucket already has " <<
			htable.get(hashFunc(tokens[2])).Count() << '\n';
    cout << "-----------------------------------" << '\n';
    htable.get(hashFunc(tokens[2])).OutputFromHead();
    cout << "-----------------------------------" << '\n';
    htable.set(Customer(tokens[0], tokens[1], tokens[2]));

    // for second hash function
    cout << "Current data is " << tokens[0] << ' ' <<
    		tokens[1] << ' ' << tokens[2] << " with hash = " <<
			hashFunc2(tokens[2]) << " and the bucket already has " <<
			htable2.get(hashFunc2(tokens[2])).Count() << '\n';
    cout << "-----------------------------------" << '\n';
    htable2.get(hashFunc2(tokens[2])).OutputFromHead();
    cout << "-----------------------------------" << '\n';
    htable2.set2(Customer(tokens[0], tokens[1], tokens[2]));

    // third hash function
    cout << "Current data is " << tokens[0] << ' ' <<
    		tokens[1] << ' ' << tokens[2] << " with hash = " <<
			hashFunc3(tokens[2]) << " and the bucket already has " <<
			htable3.get(hashFunc3(tokens[2])).Count() << '\n';
    cout << "-----------------------------------" << '\n';
    htable3.get(hashFunc3(tokens[2])).OutputFromHead();
    cout << "-----------------------------------" << '\n';
    htable3.set3(Customer(tokens[0], tokens[1], tokens[2]));

    // fourth hash function
    cout << "Current data is " << tokens[0] << ' ' <<
    		tokens[1] << ' ' << tokens[2] << " with hash = " <<
			hashFunc4(tokens[2]) << " and the bucket already has " <<
			htable4.get(hashFunc4(tokens[2])).Count() << '\n';
    cout << "-----------------------------------" << '\n';
    htable4.get(hashFunc4(tokens[2])).OutputFromHead();
    cout << "-----------------------------------" << '\n';
    htable4.set4(Customer(tokens[0], tokens[1], tokens[2]));
  }
  fin.close();
  cout << htable.getcollisions() << '\n';
  cout << htable2.getcollisions() << '\n';
  cout << htable3.getcollisions() << '\n';
  cout << htable4.getcollisions() << '\n';
  return 0;
}
