#include "Character.h"
#include <iostream>
#include <string>
#include <vector>
#include <cassert>
using namespace std;


Character::Character(string name, int health, int level)
{
    this->name = name;
    this->health = health;
    this->level = level;
}

string Character::getName()
{
    return name;
}

int Character::getHealth()
{
    return health;
}

int Character::getLevel()
{
    return level;
}

void Character::setName(string name)
{
    this->name = name;
}

void Character::setHealth(int health)
{
    this->health = health;
}

void Character::setLevel(int level)
{
    this->level = level;
}

void Character::print()
{
    cout << "Name: " << name << endl;
    cout << "Health: " << health << endl;
    cout << "Level: " << level << endl;
}

Wizard::Wizard(string name, int health, int level, int mana, vector <string> spells, int spellPower) : Character(name, health, level)
{
    this->mana = mana;
    this->spells = spells;
    this->spellPower = spellPower;
}

bool Wizard::castSpell(string spell)
{
    if (mana > 10)
    {
        mana -= 10;
        return true;
    }
    else
    {
        return false;
    }
}

Knight::Knight(string name, int health, int level, float armor, int swordDamage) : Character(name, health, level)
{
    this->armor = armor;
    this->swordDamage = swordDamage; 
}

void Knight::takeDamage(int damage)
{
    int hp = getHealth();
    hp -= damage * armor;
    setHealth(hp);
}

int main()
{
    CharacterTest::runAll();
    cout << "Character Test passed" << endl;
    WizardTest::runAll();
    cout << "Wizard Test passed" << endl;
    KnightTest::runAll();
    cout << "Knight Test passed" << endl;
    cout << "All tests passed" << endl;
    return 0;
}