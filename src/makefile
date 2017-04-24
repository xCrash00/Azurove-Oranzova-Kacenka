pack:
	zip -r  ../xdosed08_xrandy00_xwilla00.zip 	../*


test:
	cd zdroj && python3 tests.py

run:
	kalkulacka

install: ikonka
	sudo apt install python3-pip	
	sudo pip3 install PyQt5
	cd instalace && sudo dpkg -i python3-kalkulacka_0-1_all.deb 
	cd zdroj/ikonka && sudo cp kalkulacicka.desktop /usr/share/applications
	
uninstall:
	kalkulacka-odinstall.sh
	

doc:
	doxygen Doxyfile

clean:
	rm -r html && rm -r latex

ikonka:
	cd /usr/share/icons && sudo mkdir kalkulacka
	cd zdroj/ikonka && sudo cp kalkulacka.png /usr/share/icons/kalkulacka
