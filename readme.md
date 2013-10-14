Missed Connections API
======================
a crawler, redis store, and flask api for missed connections

## About the Database
`redis` is not a typical database, it's a key/value store.
to keep the api as simple as possible, our keys are unique combinations 
of city and sexual orientation (m4w, w4m, m4m, m4w, etc), and are values
are lists of json blobs, with each blob corresponding to a missed connection. 

## how to query the database?
Yes, you may be thinking this:
![img](https://pbs.twimg.com/media/BOIlOviCEAEZXTj.png:small)

But `mc-api` is pretty easy to query.  the url format is this
```
/?key=<city>:>orientation&start=<start_ts>&end=<end_ts>
```
For example: 
```
/?key=orange-county:m4w&start=0&end=10000000000
```

## LIST OF CITIES AND RSS FEEDS ##
```
auburn  -  http://auburn.craigslist.org/mis/index.rss
birmingham  -  http://bham.craigslist.org/mis/index.rss
dothan  -  http://dothan.craigslist.org/mis/index.rss
florence / muscle shoals  -  http://shoals.craigslist.org/mis/index.rss
gadsden-anniston  -  http://gadsden.craigslist.org/mis/index.rss
huntsville / decatur  -  http://huntsville.craigslist.org/mis/index.rss
mobile  -  http://mobile.craigslist.org/mis/index.rss
montgomery  -  http://montgomery.craigslist.org/mis/index.rss
tuscaloosa  -  http://tuscaloosa.craigslist.org/mis/index.rss
anchorage / mat-su  -  http://anchorage.craigslist.org/mis/index.rss
fairbanks  -  http://fairbanks.craigslist.org/mis/index.rss
kenai peninsula  -  http://kenai.craigslist.org/mis/index.rss
southeast alaska  -  http://juneau.craigslist.org/mis/index.rss
flagstaff / sedona  -  http://flagstaff.craigslist.org/mis/index.rss
mohave county  -  http://mohave.craigslist.org/mis/index.rss
phoenix  -  http://phoenix.craigslist.org/mis/index.rss
prescott  -  http://prescott.craigslist.org/mis/index.rss
show low  -  http://showlow.craigslist.org/mis/index.rss
sierra vista  -  http://sierravista.craigslist.org/mis/index.rss
tucson  -  http://tucson.craigslist.org/mis/index.rss
yuma  -  http://yuma.craigslist.org/mis/index.rss
fayetteville  -  http://fayar.craigslist.org/mis/index.rss
fort smith  -  http://fortsmith.craigslist.org/mis/index.rss
jonesboro  -  http://jonesboro.craigslist.org/mis/index.rss
little rock  -  http://littlerock.craigslist.org/mis/index.rss
texarkana  -  http://texarkana.craigslist.org/mis/index.rss
bakersfield  -  http://bakersfield.craigslist.org/mis/index.rss
chico  -  http://chico.craigslist.org/mis/index.rss
fresno / madera  -  http://fresno.craigslist.org/mis/index.rss
gold country  -  http://goldcountry.craigslist.org/mis/index.rss
hanford-corcoran  -  http://hanford.craigslist.org/mis/index.rss
humboldt county  -  http://humboldt.craigslist.org/mis/index.rss
imperial county  -  http://imperial.craigslist.org/mis/index.rss
inland empire  -  http://inlandempire.craigslist.org/mis/index.rss
los angeles  -  http://losangeles.craigslist.org/mis/index.rss
mendocino county  -  http://mendocino.craigslist.org/mis/index.rss
merced  -  http://merced.craigslist.org/mis/index.rss
modesto  -  http://modesto.craigslist.org/mis/index.rss
monterey bay  -  http://monterey.craigslist.org/mis/index.rss
orange county  -  http://orangecounty.craigslist.org/mis/index.rss
palm springs  -  http://palmsprings.craigslist.org/mis/index.rss
redding  -  http://redding.craigslist.org/mis/index.rss
sacramento  -  http://sacramento.craigslist.org/mis/index.rss
san diego  -  http://sandiego.craigslist.org/mis/index.rss
san francisco bay area  -  http://sfbay.craigslist.org/mis/index.rss
san luis obispo  -  http://slo.craigslist.org/mis/index.rss
santa barbara  -  http://santabarbara.craigslist.org/mis/index.rss
santa maria  -  http://santamaria.craigslist.org/mis/index.rss
siskiyou county  -  http://siskiyou.craigslist.org/mis/index.rss
stockton  -  http://stockton.craigslist.org/mis/index.rss
susanville  -  http://susanville.craigslist.org/mis/index.rss
ventura county  -  http://ventura.craigslist.org/mis/index.rss
visalia-tulare  -  http://visalia.craigslist.org/mis/index.rss
yuba-sutter  -  http://yubasutter.craigslist.org/mis/index.rss
boulder  -  http://boulder.craigslist.org/mis/index.rss
colorado springs  -  http://cosprings.craigslist.org/mis/index.rss
denver  -  http://denver.craigslist.org/mis/index.rss
eastern CO  -  http://eastco.craigslist.org/mis/index.rss
fort collins / north CO  -  http://fortcollins.craigslist.org/mis/index.rss
high rockies  -  http://rockies.craigslist.org/mis/index.rss
pueblo  -  http://pueblo.craigslist.org/mis/index.rss
western slope  -  http://westslope.craigslist.org/mis/index.rss
eastern CT  -  http://newlondon.craigslist.org/mis/index.rss
hartford  -  http://hartford.craigslist.org/mis/index.rss
new haven  -  http://newhaven.craigslist.org/mis/index.rss
northwest CT  -  http://nwct.craigslist.org/mis/index.rss
delaware  -  http://delaware.craigslist.org/mis/index.rss
washington  -  http://washingtondc.craigslist.org/mis/index.rss
daytona beach  -  http://daytona.craigslist.org/mis/index.rss
florida keys  -  http://keys.craigslist.org/mis/index.rss
fort lauderdale  -  http://fortlauderdale.craigslist.org/mis/index.rss
ft myers / SW florida  -  http://fortmyers.craigslist.org/mis/index.rss
gainesville  -  http://gainesville.craigslist.org/mis/index.rss
heartland florida  -  http://cfl.craigslist.org/mis/index.rss
jacksonville  -  http://jacksonville.craigslist.org/mis/index.rss
lakeland  -  http://lakeland.craigslist.org/mis/index.rss
north central FL  -  http://lakecity.craigslist.org/mis/index.rss
ocala  -  http://ocala.craigslist.org/mis/index.rss
okaloosa / walton  -  http://okaloosa.craigslist.org/mis/index.rss
orlando  -  http://orlando.craigslist.org/mis/index.rss
panama city  -  http://panamacity.craigslist.org/mis/index.rss
pensacola  -  http://pensacola.craigslist.org/mis/index.rss
sarasota-bradenton  -  http://sarasota.craigslist.org/mis/index.rss
south florida  -  http://miami.craigslist.org/mis/index.rss
space coast  -  http://spacecoast.craigslist.org/mis/index.rss
st augustine  -  http://staugustine.craigslist.org/mis/index.rss
tallahassee  -  http://tallahassee.craigslist.org/mis/index.rss
tampa bay area  -  http://tampa.craigslist.org/mis/index.rss
treasure coast  -  http://treasure.craigslist.org/mis/index.rss
west palm beach  -  http://westpalmbeach.craigslist.org/mis/index.rss
albany  -  http://albanyga.craigslist.org/mis/index.rss
athens  -  http://athensga.craigslist.org/mis/index.rss
atlanta  -  http://atlanta.craigslist.org/mis/index.rss
augusta  -  http://augusta.craigslist.org/mis/index.rss
brunswick  -  http://brunswick.craigslist.org/mis/index.rss
columbus  -  http://columbusga.craigslist.org/mis/index.rss
macon / warner robins  -  http://macon.craigslist.org/mis/index.rss
northwest GA  -  http://nwga.craigslist.org/mis/index.rss
savannah / hinesville  -  http://savannah.craigslist.org/mis/index.rss
statesboro  -  http://statesboro.craigslist.org/mis/index.rss
valdosta  -  http://valdosta.craigslist.org/mis/index.rss
hawaii  -  http://honolulu.craigslist.org/mis/index.rss
boise  -  http://boise.craigslist.org/mis/index.rss
east idaho  -  http://eastidaho.craigslist.org/mis/index.rss
lewiston / clarkston  -  http://lewiston.craigslist.org/mis/index.rss
twin falls  -  http://twinfalls.craigslist.org/mis/index.rss
bloomington-normal  -  http://bn.craigslist.org/mis/index.rss
champaign urbana  -  http://chambana.craigslist.org/mis/index.rss
chicago  -  http://chicago.craigslist.org/mis/index.rss
decatur  -  http://decatur.craigslist.org/mis/index.rss
la salle co  -  http://lasalle.craigslist.org/mis/index.rss
mattoon-charleston  -  http://mattoon.craigslist.org/mis/index.rss
peoria  -  http://peoria.craigslist.org/mis/index.rss
rockford  -  http://rockford.craigslist.org/mis/index.rss
southern illinois  -  http://carbondale.craigslist.org/mis/index.rss
springfield  -  http://springfieldil.craigslist.org/mis/index.rss
western IL  -  http://quincy.craigslist.org/mis/index.rss
bloomington  -  http://bloomington.craigslist.org/mis/index.rss
evansville  -  http://evansville.craigslist.org/mis/index.rss
fort wayne  -  http://fortwayne.craigslist.org/mis/index.rss
indianapolis  -  http://indianapolis.craigslist.org/mis/index.rss
kokomo  -  http://kokomo.craigslist.org/mis/index.rss
lafayette / west lafayette  -  http://tippecanoe.craigslist.org/mis/index.rss
muncie / anderson  -  http://muncie.craigslist.org/mis/index.rss
richmond  -  http://richmondin.craigslist.org/mis/index.rss
south bend / michiana  -  http://southbend.craigslist.org/mis/index.rss
terre haute  -  http://terrehaute.craigslist.org/mis/index.rss
ames  -  http://ames.craigslist.org/mis/index.rss
cedar rapids  -  http://cedarrapids.craigslist.org/mis/index.rss
des moines  -  http://desmoines.craigslist.org/mis/index.rss
dubuque  -  http://dubuque.craigslist.org/mis/index.rss
fort dodge  -  http://fortdodge.craigslist.org/mis/index.rss
iowa city  -  http://iowacity.craigslist.org/mis/index.rss
mason city  -  http://masoncity.craigslist.org/mis/index.rss
quad cities  -  http://quadcities.craigslist.org/mis/index.rss
sioux city  -  http://siouxcity.craigslist.org/mis/index.rss
southeast IA  -  http://ottumwa.craigslist.org/mis/index.rss
waterloo / cedar falls  -  http://waterloo.craigslist.org/mis/index.rss
lawrence  -  http://lawrence.craigslist.org/mis/index.rss
manhattan  -  http://ksu.craigslist.org/mis/index.rss
northwest KS  -  http://nwks.craigslist.org/mis/index.rss
salina  -  http://salina.craigslist.org/mis/index.rss
southeast KS  -  http://seks.craigslist.org/mis/index.rss
southwest KS  -  http://swks.craigslist.org/mis/index.rss
topeka  -  http://topeka.craigslist.org/mis/index.rss
wichita  -  http://wichita.craigslist.org/mis/index.rss
bowling green  -  http://bgky.craigslist.org/mis/index.rss
eastern kentucky  -  http://eastky.craigslist.org/mis/index.rss
lexington  -  http://lexington.craigslist.org/mis/index.rss
louisville  -  http://louisville.craigslist.org/mis/index.rss
owensboro  -  http://owensboro.craigslist.org/mis/index.rss
western KY  -  http://westky.craigslist.org/mis/index.rss
baton rouge  -  http://batonrouge.craigslist.org/mis/index.rss
central louisiana  -  http://cenla.craigslist.org/mis/index.rss
houma  -  http://houma.craigslist.org/mis/index.rss
lafayette  -  http://lafayette.craigslist.org/mis/index.rss
lake charles  -  http://lakecharles.craigslist.org/mis/index.rss
monroe  -  http://monroe.craigslist.org/mis/index.rss
new orleans  -  http://neworleans.craigslist.org/mis/index.rss
shreveport  -  http://shreveport.craigslist.org/mis/index.rss
maine  -  http://maine.craigslist.org/mis/index.rss
annapolis  -  http://annapolis.craigslist.org/mis/index.rss
baltimore  -  http://baltimore.craigslist.org/mis/index.rss
eastern shore  -  http://easternshore.craigslist.org/mis/index.rss
frederick  -  http://frederick.craigslist.org/mis/index.rss
southern maryland  -  http://smd.craigslist.org/mis/index.rss
western maryland  -  http://westmd.craigslist.org/mis/index.rss
boston  -  http://boston.craigslist.org/mis/index.rss
cape cod / islands  -  http://capecod.craigslist.org/mis/index.rss
south coast  -  http://southcoast.craigslist.org/mis/index.rss
western massachusetts  -  http://westernmass.craigslist.org/mis/index.rss
worcester / central MA  -  http://worcester.craigslist.org/mis/index.rss
ann arbor  -  http://annarbor.craigslist.org/mis/index.rss
battle creek  -  http://battlecreek.craigslist.org/mis/index.rss
central michigan  -  http://centralmich.craigslist.org/mis/index.rss
detroit metro  -  http://detroit.craigslist.org/mis/index.rss
flint  -  http://flint.craigslist.org/mis/index.rss
grand rapids  -  http://grandrapids.craigslist.org/mis/index.rss
holland  -  http://holland.craigslist.org/mis/index.rss
jackson  -  http://jxn.craigslist.org/mis/index.rss
kalamazoo  -  http://kalamazoo.craigslist.org/mis/index.rss
lansing  -  http://lansing.craigslist.org/mis/index.rss
monroe  -  http://monroemi.craigslist.org/mis/index.rss
muskegon  -  http://muskegon.craigslist.org/mis/index.rss
northern michigan  -  http://nmi.craigslist.org/mis/index.rss
port huron  -  http://porthuron.craigslist.org/mis/index.rss
saginaw-midland-baycity  -  http://saginaw.craigslist.org/mis/index.rss
southwest michigan  -  http://swmi.craigslist.org/mis/index.rss
the thumb  -  http://thumb.craigslist.org/mis/index.rss
upper peninsula  -  http://up.craigslist.org/mis/index.rss
bemidji  -  http://bemidji.craigslist.org/mis/index.rss
brainerd  -  http://brainerd.craigslist.org/mis/index.rss
duluth / superior  -  http://duluth.craigslist.org/mis/index.rss
mankato  -  http://mankato.craigslist.org/mis/index.rss
minneapolis / st paul  -  http://minneapolis.craigslist.org/mis/index.rss
rochester  -  http://rmn.craigslist.org/mis/index.rss
southwest MN  -  http://marshall.craigslist.org/mis/index.rss
st cloud  -  http://stcloud.craigslist.org/mis/index.rss
gulfport / biloxi  -  http://gulfport.craigslist.org/mis/index.rss
hattiesburg  -  http://hattiesburg.craigslist.org/mis/index.rss
jackson  -  http://jackson.craigslist.org/mis/index.rss
meridian  -  http://meridian.craigslist.org/mis/index.rss
north mississippi  -  http://northmiss.craigslist.org/mis/index.rss
southwest MS  -  http://natchez.craigslist.org/mis/index.rss
columbia / jeff city  -  http://columbiamo.craigslist.org/mis/index.rss
joplin  -  http://joplin.craigslist.org/mis/index.rss
kansas city  -  http://kansascity.craigslist.org/mis/index.rss
kirksville  -  http://kirksville.craigslist.org/mis/index.rss
lake of the ozarks  -  http://loz.craigslist.org/mis/index.rss
southeast missouri  -  http://semo.craigslist.org/mis/index.rss
springfield  -  http://springfield.craigslist.org/mis/index.rss
st joseph  -  http://stjoseph.craigslist.org/mis/index.rss
st louis  -  http://stlouis.craigslist.org/mis/index.rss
billings  -  http://billings.craigslist.org/mis/index.rss
bozeman  -  http://bozeman.craigslist.org/mis/index.rss
butte  -  http://butte.craigslist.org/mis/index.rss
great falls  -  http://greatfalls.craigslist.org/mis/index.rss
helena  -  http://helena.craigslist.org/mis/index.rss
kalispell  -  http://kalispell.craigslist.org/mis/index.rss
missoula  -  http://missoula.craigslist.org/mis/index.rss
montana (old)  -  http://montana.craigslist.org/mis/index.rss
grand island  -  http://grandisland.craigslist.org/mis/index.rss
lincoln  -  http://lincoln.craigslist.org/mis/index.rss
north platte  -  http://northplatte.craigslist.org/mis/index.rss
omaha / council bluffs  -  http://omaha.craigslist.org/mis/index.rss
scottsbluff / panhandle  -  http://scottsbluff.craigslist.org/mis/index.rss
elko  -  http://elko.craigslist.org/mis/index.rss
las vegas  -  http://lasvegas.craigslist.org/mis/index.rss
reno / tahoe  -  http://reno.craigslist.org/mis/index.rss
new hampshire  -  http://nh.craigslist.org/mis/index.rss
central NJ  -  http://cnj.craigslist.org/mis/index.rss
jersey shore  -  http://jerseyshore.craigslist.org/mis/index.rss
north jersey  -  http://newjersey.craigslist.org/mis/index.rss
south jersey  -  http://southjersey.craigslist.org/mis/index.rss
albuquerque  -  http://albuquerque.craigslist.org/mis/index.rss
clovis / portales  -  http://clovis.craigslist.org/mis/index.rss
farmington  -  http://farmington.craigslist.org/mis/index.rss
las cruces  -  http://lascruces.craigslist.org/mis/index.rss
roswell / carlsbad  -  http://roswell.craigslist.org/mis/index.rss
santa fe / taos  -  http://santafe.craigslist.org/mis/index.rss
albany  -  http://albany.craigslist.org/mis/index.rss
binghamton  -  http://binghamton.craigslist.org/mis/index.rss
buffalo  -  http://buffalo.craigslist.org/mis/index.rss
catskills  -  http://catskills.craigslist.org/mis/index.rss
chautauqua  -  http://chautauqua.craigslist.org/mis/index.rss
elmira-corning  -  http://elmira.craigslist.org/mis/index.rss
finger lakes  -  http://fingerlakes.craigslist.org/mis/index.rss
glens falls  -  http://glensfalls.craigslist.org/mis/index.rss
hudson valley  -  http://hudsonvalley.craigslist.org/mis/index.rss
ithaca  -  http://ithaca.craigslist.org/mis/index.rss
long island  -  http://longisland.craigslist.org/mis/index.rss
new york city  -  http://newyork.craigslist.org/mis/index.rss
oneonta  -  http://oneonta.craigslist.org/mis/index.rss
plattsburgh-adirondacks  -  http://plattsburgh.craigslist.org/mis/index.rss
potsdam-canton-massena  -  http://potsdam.craigslist.org/mis/index.rss
rochester  -  http://rochester.craigslist.org/mis/index.rss
syracuse  -  http://syracuse.craigslist.org/mis/index.rss
twin tiers NY/PA  -  http://twintiers.craigslist.org/mis/index.rss
utica-rome-oneida  -  http://utica.craigslist.org/mis/index.rss
watertown  -  http://watertown.craigslist.org/mis/index.rss
asheville  -  http://asheville.craigslist.org/mis/index.rss
boone  -  http://boone.craigslist.org/mis/index.rss
charlotte  -  http://charlotte.craigslist.org/mis/index.rss
eastern NC  -  http://eastnc.craigslist.org/mis/index.rss
fayetteville  -  http://fayetteville.craigslist.org/mis/index.rss
greensboro  -  http://greensboro.craigslist.org/mis/index.rss
hickory / lenoir  -  http://hickory.craigslist.org/mis/index.rss
jacksonville  -  http://onslow.craigslist.org/mis/index.rss
outer banks  -  http://outerbanks.craigslist.org/mis/index.rss
raleigh / durham / CH  -  http://raleigh.craigslist.org/mis/index.rss
wilmington  -  http://wilmington.craigslist.org/mis/index.rss
winston-salem  -  http://winstonsalem.craigslist.org/mis/index.rss
bismarck  -  http://bismarck.craigslist.org/mis/index.rss
fargo / moorhead  -  http://fargo.craigslist.org/mis/index.rss
grand forks  -  http://grandforks.craigslist.org/mis/index.rss
north dakota  -  http://nd.craigslist.org/mis/index.rss
akron / canton  -  http://akroncanton.craigslist.org/mis/index.rss
ashtabula  -  http://ashtabula.craigslist.org/mis/index.rss
athens  -  http://athensohio.craigslist.org/mis/index.rss
chillicothe  -  http://chillicothe.craigslist.org/mis/index.rss
cincinnati  -  http://cincinnati.craigslist.org/mis/index.rss
cleveland  -  http://cleveland.craigslist.org/mis/index.rss
columbus  -  http://columbus.craigslist.org/mis/index.rss
dayton / springfield  -  http://dayton.craigslist.org/mis/index.rss
lima / findlay  -  http://limaohio.craigslist.org/mis/index.rss
mansfield  -  http://mansfield.craigslist.org/mis/index.rss
sandusky  -  http://sandusky.craigslist.org/mis/index.rss
toledo  -  http://toledo.craigslist.org/mis/index.rss
tuscarawas co  -  http://tuscarawas.craigslist.org/mis/index.rss
youngstown  -  http://youngstown.craigslist.org/mis/index.rss
zanesville / cambridge  -  http://zanesville.craigslist.org/mis/index.rss
lawton  -  http://lawton.craigslist.org/mis/index.rss
northwest OK  -  http://enid.craigslist.org/mis/index.rss
oklahoma city  -  http://oklahomacity.craigslist.org/mis/index.rss
stillwater  -  http://stillwater.craigslist.org/mis/index.rss
tulsa  -  http://tulsa.craigslist.org/mis/index.rss
bend  -  http://bend.craigslist.org/mis/index.rss
corvallis/albany  -  http://corvallis.craigslist.org/mis/index.rss
east oregon  -  http://eastoregon.craigslist.org/mis/index.rss
eugene  -  http://eugene.craigslist.org/mis/index.rss
klamath falls  -  http://klamath.craigslist.org/mis/index.rss
medford-ashland  -  http://medford.craigslist.org/mis/index.rss
oregon coast  -  http://oregoncoast.craigslist.org/mis/index.rss
portland  -  http://portland.craigslist.org/mis/index.rss
roseburg  -  http://roseburg.craigslist.org/mis/index.rss
salem  -  http://salem.craigslist.org/mis/index.rss
altoona-johnstown  -  http://altoona.craigslist.org/mis/index.rss
cumberland valley  -  http://chambersburg.craigslist.org/mis/index.rss
erie  -  http://erie.craigslist.org/mis/index.rss
harrisburg  -  http://harrisburg.craigslist.org/mis/index.rss
lancaster  -  http://lancaster.craigslist.org/mis/index.rss
lehigh valley  -  http://allentown.craigslist.org/mis/index.rss
meadville  -  http://meadville.craigslist.org/mis/index.rss
philadelphia  -  http://philadelphia.craigslist.org/mis/index.rss
pittsburgh  -  http://pittsburgh.craigslist.org/mis/index.rss
poconos  -  http://poconos.craigslist.org/mis/index.rss
reading  -  http://reading.craigslist.org/mis/index.rss
scranton / wilkes-barre  -  http://scranton.craigslist.org/mis/index.rss
state college  -  http://pennstate.craigslist.org/mis/index.rss
williamsport  -  http://williamsport.craigslist.org/mis/index.rss
york  -  http://york.craigslist.org/mis/index.rss
rhode island  -  http://providence.craigslist.org/mis/index.rss
charleston  -  http://charleston.craigslist.org/mis/index.rss
columbia  -  http://columbia.craigslist.org/mis/index.rss
florence  -  http://florencesc.craigslist.org/mis/index.rss
greenville / upstate  -  http://greenville.craigslist.org/mis/index.rss
hilton head  -  http://hiltonhead.craigslist.org/mis/index.rss
myrtle beach  -  http://myrtlebeach.craigslist.org/mis/index.rss
northeast SD  -  http://nesd.craigslist.org/mis/index.rss
pierre / central SD  -  http://csd.craigslist.org/mis/index.rss
rapid city / west SD  -  http://rapidcity.craigslist.org/mis/index.rss
sioux falls / SE SD  -  http://siouxfalls.craigslist.org/mis/index.rss
south dakota  -  http://sd.craigslist.org/mis/index.rss
chattanooga  -  http://chattanooga.craigslist.org/mis/index.rss
clarksville  -  http://clarksville.craigslist.org/mis/index.rss
cookeville  -  http://cookeville.craigslist.org/mis/index.rss
jackson  -  http://jacksontn.craigslist.org/mis/index.rss
knoxville  -  http://knoxville.craigslist.org/mis/index.rss
memphis  -  http://memphis.craigslist.org/mis/index.rss
nashville  -  http://nashville.craigslist.org/mis/index.rss
tri-cities  -  http://tricities.craigslist.org/mis/index.rss
abilene  -  http://abilene.craigslist.org/mis/index.rss
amarillo  -  http://amarillo.craigslist.org/mis/index.rss
austin  -  http://austin.craigslist.org/mis/index.rss
beaumont / port arthur  -  http://beaumont.craigslist.org/mis/index.rss
brownsville  -  http://brownsville.craigslist.org/mis/index.rss
college station  -  http://collegestation.craigslist.org/mis/index.rss
corpus christi  -  http://corpuschristi.craigslist.org/mis/index.rss
dallas / fort worth  -  http://dallas.craigslist.org/mis/index.rss
deep east texas  -  http://nacogdoches.craigslist.org/mis/index.rss
del rio / eagle pass  -  http://delrio.craigslist.org/mis/index.rss
el paso  -  http://elpaso.craigslist.org/mis/index.rss
galveston  -  http://galveston.craigslist.org/mis/index.rss
houston  -  http://houston.craigslist.org/mis/index.rss
killeen / temple / ft hood  -  http://killeen.craigslist.org/mis/index.rss
laredo  -  http://laredo.craigslist.org/mis/index.rss
lubbock  -  http://lubbock.craigslist.org/mis/index.rss
mcallen / edinburg  -  http://mcallen.craigslist.org/mis/index.rss
odessa / midland  -  http://odessa.craigslist.org/mis/index.rss
san angelo  -  http://sanangelo.craigslist.org/mis/index.rss
san antonio  -  http://sanantonio.craigslist.org/mis/index.rss
san marcos  -  http://sanmarcos.craigslist.org/mis/index.rss
southwest TX  -  http://bigbend.craigslist.org/mis/index.rss
texoma  -  http://texoma.craigslist.org/mis/index.rss
tyler / east TX  -  http://easttexas.craigslist.org/mis/index.rss
victoria  -  http://victoriatx.craigslist.org/mis/index.rss
waco  -  http://waco.craigslist.org/mis/index.rss
wichita falls  -  http://wichitafalls.craigslist.org/mis/index.rss
logan  -  http://logan.craigslist.org/mis/index.rss
ogden-clearfield  -  http://ogden.craigslist.org/mis/index.rss
provo / orem  -  http://provo.craigslist.org/mis/index.rss
salt lake city  -  http://saltlakecity.craigslist.org/mis/index.rss
st george  -  http://stgeorge.craigslist.org/mis/index.rss
vermont  -  http://burlington.craigslist.org/mis/index.rss
charlottesville  -  http://charlottesville.craigslist.org/mis/index.rss
danville  -  http://danville.craigslist.org/mis/index.rss
fredericksburg  -  http://fredericksburg.craigslist.org/mis/index.rss
hampton roads  -  http://norfolk.craigslist.org/mis/index.rss
harrisonburg  -  http://harrisonburg.craigslist.org/mis/index.rss
lynchburg  -  http://lynchburg.craigslist.org/mis/index.rss
new river valley  -  http://blacksburg.craigslist.org/mis/index.rss
richmond  -  http://richmond.craigslist.org/mis/index.rss
roanoke  -  http://roanoke.craigslist.org/mis/index.rss
southwest VA  -  http://swva.craigslist.org/mis/index.rss
winchester  -  http://winchester.craigslist.org/mis/index.rss
bellingham  -  http://bellingham.craigslist.org/mis/index.rss
kennewick-pasco-richland  -  http://kpr.craigslist.org/mis/index.rss
moses lake  -  http://moseslake.craigslist.org/mis/index.rss
olympic peninsula  -  http://olympic.craigslist.org/mis/index.rss
pullman / moscow  -  http://pullman.craigslist.org/mis/index.rss
seattle-tacoma  -  http://seattle.craigslist.org/mis/index.rss
skagit / island / SJI  -  http://skagit.craigslist.org/mis/index.rss
spokane / coeur d'alene  -  http://spokane.craigslist.org/mis/index.rss
wenatchee  -  http://wenatchee.craigslist.org/mis/index.rss
yakima  -  http://yakima.craigslist.org/mis/index.rss
charleston  -  http://charlestonwv.craigslist.org/mis/index.rss
eastern panhandle  -  http://martinsburg.craigslist.org/mis/index.rss
huntington-ashland  -  http://huntington.craigslist.org/mis/index.rss
morgantown  -  http://morgantown.craigslist.org/mis/index.rss
northern panhandle  -  http://wheeling.craigslist.org/mis/index.rss
parkersburg-marietta  -  http://parkersburg.craigslist.org/mis/index.rss
southern WV  -  http://swv.craigslist.org/mis/index.rss
west virginia (old)  -  http://wv.craigslist.org/mis/index.rss
appleton-oshkosh-FDL  -  http://appleton.craigslist.org/mis/index.rss
eau claire  -  http://eauclaire.craigslist.org/mis/index.rss
green bay  -  http://greenbay.craigslist.org/mis/index.rss
janesville  -  http://janesville.craigslist.org/mis/index.rss
kenosha-racine  -  http://racine.craigslist.org/mis/index.rss
la crosse  -  http://lacrosse.craigslist.org/mis/index.rss
madison  -  http://madison.craigslist.org/mis/index.rss
milwaukee  -  http://milwaukee.craigslist.org/mis/index.rss
northern WI  -  http://northernwi.craigslist.org/mis/index.rss
sheboygan  -  http://sheboygan.craigslist.org/mis/index.rss
wausau  -  http://wausau.craigslist.org/mis/index.rss
wyoming  -  http://wyoming.craigslist.org/mis/index.rss
guam-micronesia  -  http://micronesia.craigslist.org/mis/index.rss
puerto rico  -  http://puertorico.craigslist.org/mis/index.rss
U.S. virgin islands  -  http://virgin.craigslist.org/mis/index.rss
calgary  -  http://calgary.craigslist.ca/mis/index.rss
edmonton  -  http://edmonton.craigslist.ca/mis/index.rss
ft mcmurray  -  http://ftmcmurray.craigslist.ca/mis/index.rss
lethbridge  -  http://lethbridge.craigslist.ca/mis/index.rss
medicine hat  -  http://hat.craigslist.ca/mis/index.rss
peace river country  -  http://peace.craigslist.ca/mis/index.rss
red deer  -  http://reddeer.craigslist.ca/mis/index.rss
cariboo  -  http://cariboo.craigslist.ca/mis/index.rss
comox valley  -  http://comoxvalley.craigslist.ca/mis/index.rss
fraser valley  -  http://abbotsford.craigslist.ca/mis/index.rss
kamloops  -  http://kamloops.craigslist.ca/mis/index.rss
kelowna / okanagan  -  http://kelowna.craigslist.ca/mis/index.rss
kootenays  -  http://cranbrook.craigslist.ca/mis/index.rss
nanaimo  -  http://nanaimo.craigslist.ca/mis/index.rss
prince george  -  http://princegeorge.craigslist.ca/mis/index.rss
skeena-bulkley  -  http://skeena.craigslist.ca/mis/index.rss
sunshine coast  -  http://sunshine.craigslist.ca/mis/index.rss
vancouver  -  http://vancouver.craigslist.ca/mis/index.rss
victoria  -  http://victoria.craigslist.ca/mis/index.rss
whistler  -  http://whistler.craigslist.ca/mis/index.rss
winnipeg  -  http://winnipeg.craigslist.ca/mis/index.rss
new brunswick  -  http://newbrunswick.craigslist.ca/mis/index.rss
st john's  -  http://newfoundland.craigslist.ca/mis/index.rss
territories  -  http://territories.craigslist.ca/mis/index.rss
yellowknife  -  http://yellowknife.craigslist.ca/mis/index.rss
halifax  -  http://halifax.craigslist.ca/mis/index.rss
barrie  -  http://barrie.craigslist.ca/mis/index.rss
belleville  -  http://belleville.craigslist.ca/mis/index.rss
brantford-woodstock  -  http://brantford.craigslist.ca/mis/index.rss
chatham-kent  -  http://chatham.craigslist.ca/mis/index.rss
cornwall  -  http://cornwall.craigslist.ca/mis/index.rss
guelph  -  http://guelph.craigslist.ca/mis/index.rss
hamilton-burlington  -  http://hamilton.craigslist.ca/mis/index.rss
kingston  -  http://kingston.craigslist.ca/mis/index.rss
kitchener-waterloo-cambridge  -  http://kitchener.craigslist.ca/mis/index.rss
london  -  http://londonon.craigslist.ca/mis/index.rss
niagara region  -  http://niagara.craigslist.ca/mis/index.rss
ottawa-hull-gatineau  -  http://ottawa.craigslist.ca/mis/index.rss
owen sound  -  http://owensound.craigslist.ca/mis/index.rss
peterborough  -  http://peterborough.craigslist.ca/mis/index.rss
sarnia  -  http://sarnia.craigslist.ca/mis/index.rss
sault ste marie  -  http://soo.craigslist.ca/mis/index.rss
sudbury  -  http://sudbury.craigslist.ca/mis/index.rss
thunder bay  -  http://thunderbay.craigslist.ca/mis/index.rss
toronto  -  http://toronto.craigslist.ca/mis/index.rss
windsor  -  http://windsor.craigslist.ca/mis/index.rss
prince edward island  -  http://pei.craigslist.ca/mis/index.rss
montreal  -  http://montreal.craigslist.ca/mis/index.rss
quebec city  -  http://quebec.craigslist.ca/mis/index.rss
saguenay  -  http://saguenay.craigslist.ca/mis/index.rss
sherbrooke  -  http://sherbrooke.craigslist.ca/mis/index.rss
trois-rivieres  -  http://troisrivieres.craigslist.ca/mis/index.rss
regina  -  http://regina.craigslist.ca/mis/index.rss
saskatoon  -  http://saskatoon.craigslist.ca/mis/index.rss
whitehorse  -  http://whitehorse.craigslist.ca/mis/index.rss
vienna  -  http://vienna.craigslist.at/mis/index.rss
belgium  -  http://brussels.craigslist.org/mis/index.rss
bulgaria  -  http://bulgaria.craigslist.org/mis/index.rss
croatia  -  http://zagreb.craigslist.org/mis/index.rss
prague  -  http://prague.craigslist.cz/mis/index.rss
copenhagen  -  http://copenhagen.craigslist.org/mis/index.rss
finland  -  http://helsinki.craigslist.fi/mis/index.rss
bordeaux  -  http://bordeaux.craigslist.org/mis/index.rss
brittany  -  http://rennes.craigslist.org/mis/index.rss
grenoble  -  http://grenoble.craigslist.org/mis/index.rss
lille  -  http://lille.craigslist.org/mis/index.rss
loire valley  -  http://loire.craigslist.org/mis/index.rss
lyon  -  http://lyon.craigslist.org/mis/index.rss
marseille  -  http://marseilles.craigslist.org/mis/index.rss
montpellier  -  http://montpellier.craigslist.org/mis/index.rss
nice / cote d'azur  -  http://cotedazur.craigslist.org/mis/index.rss
normandy  -  http://rouen.craigslist.org/mis/index.rss
paris  -  http://paris.craigslist.org/mis/index.rss
strasbourg  -  http://strasbourg.craigslist.org/mis/index.rss
toulouse  -  http://toulouse.craigslist.org/mis/index.rss
berlin  -  http://berlin.craigslist.de/mis/index.rss
bremen  -  http://bremen.craigslist.de/mis/index.rss
cologne  -  http://cologne.craigslist.de/mis/index.rss
dresden  -  http://dresden.craigslist.de/mis/index.rss
dusseldorf  -  http://dusseldorf.craigslist.de/mis/index.rss
essen / ruhr  -  http://essen.craigslist.de/mis/index.rss
frankfurt  -  http://frankfurt.craigslist.de/mis/index.rss
hamburg  -  http://hamburg.craigslist.de/mis/index.rss
hannover  -  http://hannover.craigslist.de/mis/index.rss
heidelberg  -  http://heidelberg.craigslist.de/mis/index.rss
kaiserslautern  -  http://kaiserslautern.craigslist.de/mis/index.rss
leipzig  -  http://leipzig.craigslist.de/mis/index.rss
munich  -  http://munich.craigslist.de/mis/index.rss
nuremberg  -  http://nuremberg.craigslist.de/mis/index.rss
stuttgart  -  http://stuttgart.craigslist.de/mis/index.rss
greece  -  http://athens.craigslist.gr/mis/index.rss
budapest  -  http://budapest.craigslist.org/mis/index.rss
reykjavik  -  http://reykjavik.craigslist.org/mis/index.rss
dublin  -  http://dublin.craigslist.org/mis/index.rss
bologna  -  http://bologna.craigslist.it/mis/index.rss
florence / tuscany  -  http://florence.craigslist.it/mis/index.rss
genoa  -  http://genoa.craigslist.it/mis/index.rss
milan  -  http://milan.craigslist.it/mis/index.rss
napoli / campania  -  http://naples.craigslist.it/mis/index.rss
perugia  -  http://perugia.craigslist.it/mis/index.rss
rome  -  http://rome.craigslist.it/mis/index.rss
sardinia  -  http://sardinia.craigslist.it/mis/index.rss
sicilia  -  http://sicily.craigslist.it/mis/index.rss
torino  -  http://torino.craigslist.it/mis/index.rss
venice / veneto  -  http://venice.craigslist.it/mis/index.rss
luxembourg  -  http://luxembourg.craigslist.org/mis/index.rss
amsterdam / randstad  -  http://amsterdam.craigslist.org/mis/index.rss
norway  -  http://oslo.craigslist.org/mis/index.rss
poland  -  http://warsaw.craigslist.pl/mis/index.rss
faro / algarve  -  http://faro.craigslist.pt/mis/index.rss
lisbon  -  http://lisbon.craigslist.pt/mis/index.rss
porto  -  http://porto.craigslist.pt/mis/index.rss
romania  -  http://bucharest.craigslist.org/mis/index.rss
moscow  -  http://moscow.craigslist.org/mis/index.rss
st petersburg  -  http://stpetersburg.craigslist.org/mis/index.rss
alicante  -  http://alicante.craigslist.es/mis/index.rss
baleares  -  http://baleares.craigslist.es/mis/index.rss
barcelona  -  http://barcelona.craigslist.es/mis/index.rss
bilbao  -  http://bilbao.craigslist.es/mis/index.rss
cadiz  -  http://cadiz.craigslist.es/mis/index.rss
canarias  -  http://canarias.craigslist.es/mis/index.rss
granada  -  http://granada.craigslist.es/mis/index.rss
madrid  -  http://madrid.craigslist.es/mis/index.rss
malaga  -  http://malaga.craigslist.es/mis/index.rss
sevilla  -  http://sevilla.craigslist.es/mis/index.rss
valencia  -  http://valencia.craigslist.es/mis/index.rss
sweden  -  http://stockholm.craigslist.se/mis/index.rss
basel  -  http://basel.craigslist.ch/mis/index.rss
bern  -  http://bern.craigslist.ch/mis/index.rss
geneva  -  http://geneva.craigslist.ch/mis/index.rss
lausanne  -  http://lausanne.craigslist.ch/mis/index.rss
zurich  -  http://zurich.craigslist.ch/mis/index.rss
turkey  -  http://istanbul.craigslist.com.tr/mis/index.rss
ukraine  -  http://ukraine.craigslist.org/mis/index.rss
aberdeen  -  http://aberdeen.craigslist.co.uk/mis/index.rss
bath  -  http://bath.craigslist.co.uk/mis/index.rss
belfast  -  http://belfast.craigslist.co.uk/mis/index.rss
birmingham / west mids  -  http://birmingham.craigslist.co.uk/mis/index.rss
brighton  -  http://brighton.craigslist.co.uk/mis/index.rss
bristol  -  http://bristol.craigslist.co.uk/mis/index.rss
"cambridge  -  http://cambridge.craigslist.co.uk/mis/index.rss
cardiff / wales  -  http://cardiff.craigslist.co.uk/mis/index.rss
coventry  -  http://coventry.craigslist.co.uk/mis/index.rss
derby  -  http://derby.craigslist.co.uk/mis/index.rss
devon & cornwall  -  http://devon.craigslist.co.uk/mis/index.rss
dundee  -  http://dundee.craigslist.co.uk/mis/index.rss
east anglia  -  http://norwich.craigslist.co.uk/mis/index.rss
east midlands  -  http://eastmids.craigslist.co.uk/mis/index.rss
edinburgh  -  http://edinburgh.craigslist.co.uk/mis/index.rss
essex  -  http://essex.craigslist.co.uk/mis/index.rss
glasgow  -  http://glasgow.craigslist.co.uk/mis/index.rss
hampshire  -  http://hampshire.craigslist.co.uk/mis/index.rss
kent  -  http://kent.craigslist.co.uk/mis/index.rss
leeds  -  http://leeds.craigslist.co.uk/mis/index.rss
liverpool  -  http://liverpool.craigslist.co.uk/mis/index.rss
london  -  http://london.craigslist.co.uk/mis/index.rss
manchester  -  http://manchester.craigslist.co.uk/mis/index.rss
newcastle / NE england  -  http://newcastle.craigslist.co.uk/mis/index.rss
nottingham  -  http://nottingham.craigslist.co.uk/mis/index.rss
oxford  -  http://oxford.craigslist.co.uk/mis/index.rss
sheffield  -  http://sheffield.craigslist.co.uk/mis/index.rss
bangladesh  -  http://bangladesh.craigslist.org/mis/index.rss
beijing  -  http://beijing.craigslist.com.cn/mis/index.rss
chengdu  -  http://chengdu.craigslist.com.cn/mis/index.rss
chongqing  -  http://chongqing.craigslist.com.cn/mis/index.rss
dalian  -  http://dalian.craigslist.com.cn/mis/index.rss
guangzhou  -  http://guangzhou.craigslist.com.cn/mis/index.rss
hangzhou  -  http://hangzhou.craigslist.com.cn/mis/index.rss
nanjing  -  http://nanjing.craigslist.com.cn/mis/index.rss
shanghai  -  http://shanghai.craigslist.com.cn/mis/index.rss
shenyang  -  http://shenyang.craigslist.com.cn/mis/index.rss
shenzhen  -  http://shenzhen.craigslist.com.cn/mis/index.rss
wuhan  -  http://wuhan.craigslist.com.cn/mis/index.rss
xi'an  -  http://xian.craigslist.com.cn/mis/index.rss
hong kong  -  http://hongkong.craigslist.hk/mis/index.rss
ahmedabad  -  http://ahmedabad.craigslist.co.in/mis/index.rss
bangalore  -  http://bangalore.craigslist.co.in/mis/index.rss
bhubaneswar  -  http://bhubaneswar.craigslist.co.in/mis/index.rss
chandigarh  -  http://chandigarh.craigslist.co.in/mis/index.rss
chennai (madras)  -  http://chennai.craigslist.co.in/mis/index.rss
delhi  -  http://delhi.craigslist.co.in/mis/index.rss
goa  -  http://goa.craigslist.co.in/mis/index.rss
hyderabad  -  http://hyderabad.craigslist.co.in/mis/index.rss
indore  -  http://indore.craigslist.co.in/mis/index.rss
jaipur  -  http://jaipur.craigslist.co.in/mis/index.rss
kerala  -  http://kerala.craigslist.co.in/mis/index.rss
kolkata (calcutta)  -  http://kolkata.craigslist.co.in/mis/index.rss
lucknow  -  http://lucknow.craigslist.co.in/mis/index.rss
mumbai  -  http://mumbai.craigslist.co.in/mis/index.rss
pune  -  http://pune.craigslist.co.in/mis/index.rss
surat surat  -  http://surat.craigslist.co.in/mis/index.rss
indonesia  -  http://jakarta.craigslist.org/mis/index.rss
iran  -  http://tehran.craigslist.org/mis/index.rss
iraq  -  http://baghdad.craigslist.org/mis/index.rss
haifa  -  http://haifa.craigslist.org/mis/index.rss
jerusalem  -  http://jerusalem.craigslist.org/mis/index.rss
tel aviv  -  http://telaviv.craigslist.org/mis/index.rss
west bank  -  http://ramallah.craigslist.org/mis/index.rss
fukuoka  -  http://fukuoka.craigslist.jp/mis/index.rss
hiroshima  -  http://hiroshima.craigslist.jp/mis/index.rss
nagoya  -  http://nagoya.craigslist.jp/mis/index.rss
okinawa  -  http://okinawa.craigslist.jp/mis/index.rss
osaka-kobe-kyoto  -  http://osaka.craigslist.jp/mis/index.rss
sapporo  -  http://sapporo.craigslist.jp/mis/index.rss
sendai  -  http://sendai.craigslist.jp/mis/index.rss
tokyo  -  http://tokyo.craigslist.jp/mis/index.rss
seoul  -  http://seoul.craigslist.co.kr/mis/index.rss
kuwait  -  http://kuwait.craigslist.org/mis/index.rss
"beirut  -  http://beirut.craigslist.org/mis/index.rss
malaysia  -  http://malaysia.craigslist.org/mis/index.rss
pakistan  -  http://pakistan.craigslist.org/mis/index.rss
bacolod  -  http://bacolod.craigslist.com.ph/mis/index.rss
bicol region  -  http://naga.craigslist.com.ph/mis/index.rss
cagayan de oro  -  http://cdo.craigslist.com.ph/mis/index.rss
cebu  -  http://cebu.craigslist.com.ph/mis/index.rss
davao city  -  http://davaocity.craigslist.com.ph/mis/index.rss
iloilo  -  http://iloilo.craigslist.com.ph/mis/index.rss
manila  -  http://manila.craigslist.com.ph/mis/index.rss
pampanga  -  http://pampanga.craigslist.com.ph/mis/index.rss
zamboanga  -  http://zamboanga.craigslist.com.ph/mis/index.rss
singapore  -  http://singapore.craigslist.com.sg/mis/index.rss
taiwan  -  http://taipei.craigslist.com.tw/mis/index.rss
thailand  -  http://bangkok.craigslist.co.th/mis/index.rss
united arab emirates  -  http://dubai.craigslist.org/mis/index.rss
vietnam  -  http://vietnam.craigslist.org/mis/index.rss
adelaide  -  http://adelaide.craigslist.com.au/mis/index.rss
brisbane  -  http://brisbane.craigslist.com.au/mis/index.rss
cairns  -  http://cairns.craigslist.com.au/mis/index.rss
canberra  -  http://canberra.craigslist.com.au/mis/index.rss
darwin  -  http://darwin.craigslist.com.au/mis/index.rss
gold coast  -  http://goldcoast.craigslist.com.au/mis/index.rss
melbourne  -  http://melbourne.craigslist.com.au/mis/index.rss
"newcastle  -  http://ntl.craigslist.com.au/mis/index.rss
perth  -  http://perth.craigslist.com.au/mis/index.rss
sydney  -  http://sydney.craigslist.com.au/mis/index.rss
tasmania  -  http://hobart.craigslist.com.au/mis/index.rss
wollongong  -  http://wollongong.craigslist.com.au/mis/index.rss
auckland  -  http://auckland.craigslist.org/mis/index.rss
christchurch  -  http://christchurch.craigslist.org/mis/index.rss
dunedin  -  http://dunedin.craigslist.co.nz/mis/index.rss
wellington  -  http://wellington.craigslist.org/mis/index.rss
caribbean islands  -  http://caribbean.craigslist.org/mis/index.rss
buenos aires  -  http://buenosaires.craigslist.org/mis/index.rss
bolivia  -  http://lapaz.craigslist.org/mis/index.rss
belo horizonte  -  http://belohorizonte.craigslist.org/mis/index.rss
brasilia  -  http://brasilia.craigslist.org/mis/index.rss
curitiba  -  http://curitiba.craigslist.org/mis/index.rss
fortaleza  -  http://fortaleza.craigslist.org/mis/index.rss
porto alegre  -  http://portoalegre.craigslist.org/mis/index.rss
recife  -  http://recife.craigslist.org/mis/index.rss
rio de janeiro  -  http://rio.craigslist.org/mis/index.rss
"salvador  -  http://salvador.craigslist.org/mis/index.rss
sao paulo  -  http://saopaulo.craigslist.org/mis/index.rss
chile  -  http://santiago.craigslist.org/mis/index.rss
colombia  -  http://colombia.craigslist.org/mis/index.rss
costa rica  -  http://costarica.craigslist.org/mis/index.rss
dominican republic  -  http://santodomingo.craigslist.org/mis/index.rss
ecuador  -  http://quito.craigslist.org/mis/index.rss
el salvador  -  http://elsalvador.craigslist.org/mis/index.rss
guatemala  -  http://guatemala.craigslist.org/mis/index.rss
acapulco  -  http://acapulco.craigslist.com.mx/mis/index.rss
baja california sur  -  http://bajasur.craigslist.com.mx/mis/index.rss
chihuahua  -  http://chihuahua.craigslist.com.mx/mis/index.rss
ciudad juarez  -  http://juarez.craigslist.com.mx/mis/index.rss
guadalajara  -  http://guadalajara.craigslist.com.mx/mis/index.rss
guanajuato  -  http://guanajuato.craigslist.com.mx/mis/index.rss
hermosillo  -  http://hermosillo.craigslist.com.mx/mis/index.rss
mazatlan  -  http://mazatlan.craigslist.com.mx/mis/index.rss
mexico city  -  http://mexicocity.craigslist.com.mx/mis/index.rss
monterrey  -  http://monterrey.craigslist.com.mx/mis/index.rss
oaxaca  -  http://oaxaca.craigslist.com.mx/mis/index.rss
puebla  -  http://puebla.craigslist.com.mx/mis/index.rss
puerto vallarta  -  http://pv.craigslist.com.mx/mis/index.rss
tijuana  -  http://tijuana.craigslist.com.mx/mis/index.rss
veracruz  -  http://veracruz.craigslist.com.mx/mis/index.rss
yucatan  -  http://yucatan.craigslist.com.mx/mis/index.rss
nicaragua  -  http://managua.craigslist.org/mis/index.rss
panama  -  http://panama.craigslist.org/mis/index.rss
peru  -  http://lima.craigslist.org/mis/index.rss
montevideo  -  http://montevideo.craigslist.org/mis/index.rss
venezuela  -  http://caracas.craigslist.org/mis/index.rss
virgin islands  -  http://virgin.craigslist.org/mis/index.rss
egypt  -  http://cairo.craigslist.org/mis/index.rss
ethiopia  -  http://addisababa.craigslist.org/mis/index.rss
ghana  -  http://accra.craigslist.org/mis/index.rss
kenya  -  http://kenya.craigslist.org/mis/index.rss
morocco  -  http://casablanca.craigslist.org/mis/index.rss
cape town  -  http://capetown.craigslist.co.za/mis/index.rss
durban  -  http://durban.craigslist.co.za/mis/index.rss
johannesburg  -  http://johannesburg.craigslist.co.za/mis/index.rss
pretoria  -  http://pretoria.craigslist.co.za/mis/index.rss
tunisia  -  http://tunis.craigslist.org/mis/index.rss
```