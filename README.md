# AutoResume
## Introduction
AutoResume is a simle resumé generator. It is built to provide programers an easy way to generate a resumé and if necessary adjust template to his or her needs.

The vision of AutoResume is to built a free tool to generate resumés with 100% flexibility by providing an access to its code
so everyone can reaarange it however it floots his boat.
<p align="center">
    <img src="https://i.imgur.com/TBKzjAS.png"/>
</p>

## Installation
1. Pull project
```
git pull https://github.com/Murtrag/AutoResume.git
```
2. Install requirements
```
pip3 install -r requirements.txt
```
3. Make migrations
```
./manage.py migrate
```
4. You are ready to go :)
## Usage
### Set up new resumé sheet 
One should manage resumés data from django admin `http://project-address.com/admin`
<br />
<img src="https://imgur.com/nVvadIj.png"/>
<br />
* In Basic Info view we can create a brand new resumé sheet
* In Git hub buttos we can attach a link address to our git hub button
* New Sections should be created in Sections view and all its sub elements
* Graph items, List items & Section content are sub models of Sections and you can visit this places in order to modify already created elements of Section

*__NOTE:__ When you create a section element and create new section content element it shouldn't have all fields filled up but only those related to Section's `section type` field
so for `text` value you should fill up only `Section type's` Text field, for `list` value list item field and for `graph` graph item*

### Set up buttons
<br />
<img src="https://imgur.com/t0r5SCr.png"/>
<br />
All buttons should be initiated from `Types` section so the items and images through items manager.



<!-- ## Goals -->
## License
MIT License.
