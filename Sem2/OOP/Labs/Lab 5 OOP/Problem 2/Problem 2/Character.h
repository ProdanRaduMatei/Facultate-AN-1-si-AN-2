#include<string>
#include<vector>
#include<cassert>
#include <iostream>
using namespace std;

class Character{

   // TODO Character implementation
public:
    Character(std::string name, int health, int level);
    std::string getName();
    int getHealth();
    int getLevel();
    void setName(std::string name);
    void setHealth(int health);
    void setLevel(int level);
    void print();

private:
   string name;
   // other attributes here
    int health;
    int level;
   // the tester class is a friend of the Character class
   friend class CharacterTest;
};

class CharacterTest{
    // TODO CharacterTest implementation
public:
   static void testSetName(){
       // TODO your code here
         Character c("John", 100, 1);
            c.setName("Jack");
            assert(c.getName() == "Jack");
            cout << "testSetName passed" << endl;
   }
   // TODO other test methods
    static void testSetHealth(){
        Character c("John", 100, 1);
        c.setHealth(200);
        assert(c.getHealth() == 200);
        cout << "testSetHealth passed" << endl;
    }

    static void testSetLevel(){
        Character c("John", 100, 1);
        c.setLevel(2);
        assert(c.getLevel() == 2);
        cout << "testSetLevel passed" << endl;
    }

    static void testPrint(){
        Character c("John", 100, 1);
        c.print();
        cout << "testPrint passed" << endl;
    }

   static void runAll(){
       // TODO call all the other methods
        testSetName();
        testSetHealth();
        testSetLevel();
        testPrint();
   }

};

class Wizard : public Character{
   // TODO Wizard implementation
   public:
    Wizard(std::string name, int health, int level, int mana, std::vector <std::string> spells, int spellPower);
    bool castSpell(std::string spell);

private:
    int mana;
    std::vector <std::string> spells;
    int spellPower;
};

class WizardTest{
    // TODO WizardTest implementation
public:
    static void testCastSpell(){
        Wizard w("John", 100, 1, 100, {"fireball", "lightning"}, 10);
        assert(w.castSpell("fireball") == true);
        assert(w.castSpell("lightning") == true);
        // assert(w.castSpell("iceball") == false);
        cout << "testCastSpell passed" << endl;
    }

    static void runAll(){
        testCastSpell();
    }
};

class Knight : public Character{
    // TODO Knight implementation
public:
    Knight(std::string name, int health, int level, float armor, int swordDamage);
    void takeDamage(int damage);

private:
    float armor;
    int swordDamage;
};

class KnightTest{
    // TODO KnightTest implementation
public:
    static void testTakeDamage(){
        Knight k("John", 100, 1, 0.5, 10);
        k.takeDamage(10);
        assert(k.getHealth() == 95);
        k.takeDamage(10);
        assert(k.getHealth() == 90);
        cout << "testTakeDamage passed" << endl;
    }

    static void runAll(){
        testTakeDamage();
    }
};