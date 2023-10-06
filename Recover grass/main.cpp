#include <iostream>
#include <fstream>
#include <string>

//git log --pretty=format:"%h = %an , %ar : %s" --graph > result

int main()
{
	std::ifstream	readFile;
	std::ofstream	printFile;
	std::string		str;
	std::string		sub;
	std::string		shell = "git rebase -i --rebase-merges ";

	readFile.open("result");
	std::string filename = "result_";
	printFile.open(filename);
	while (!readFile.eof())
	{
		std::getline(readFile, str);
		sub = shell + str.substr(2, 6);
		printFile << sub << std::endl;
		str.clear();
	}
	readFile.close();
	printFile.close();
}