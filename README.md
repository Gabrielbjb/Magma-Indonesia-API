# Magma-Indonesia-API
![MagmaAPI](https://user-images.githubusercontent.com/111344809/216641859-80dd49db-c20a-4135-b06d-d68462235df7.png)
Welcome to Magma-Indonesia-API! This code can give you information about volcano in Indonesia! We scraped the 'https://magma.esdm.go.id/v1/gunung-api/tingkat-aktivitas website to get this information. You might ask "what is this package for?". It has a lot of uses, you can use it for educational purposes or even create an early warning systems. For example, you can check out my [Discord bot project](https://www.gabrielbjb.my.id/id/Projek/Pendeteksi_Gempa/), where users can monitor volcano activity through Discord.

## Download
If you want to try this code, you can download it by writing this on CMD, PowerShell or Terminal
### Stable
```powershell
PS> pip install Magma-Indonesia-API
```
### Requirement
requests
```powershell
PS> pip install requests
```
beautifulsoup
```powershell
PS> pip install beautifulsoup4
```

# How to use it
There are two codes that you can use:

## Level only
This code will show you the level of the volcano and the website link! Use this code if you want to get info quickly
```python
import Magma
print(Magma.magmalevelonly())
```

The output will look like this:
```json
{
   "Level IV (Awas)":{
      
   },
   "Level III (Siaga)":{
      "Anak Krakatau":{
         "location":"Lampung",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214150?signature=7938285319e0301c283407938f5b6bf7d3b74139dbea51c08ca3f17c8e2a7234"
      },
      "Merapi":{
         "location":"Daerah Istimewa Yogyakarta dan Jawa Tengah",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214152?signature=eb7e4dc8a452d8945fdcf6d52062c102587b8409b98ba4691696a9f3db996342"
      },
      "Semeru":{
         "location":"Jawa Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214151?signature=f3d92693bbeaf428ea5131e3acf29cc9f2c60a8499353e6d0244b6648908290e"
      }
   },
   "Level II (Waspada)":{
      "Awu":{
         "location":"Sulawesi Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214070?signature=6e72308ad15a889976904bb08e35b4b1d57e8e75e80021000fdf8601bb01c59d"
      },
      "Banda Api":{
         "location":"Maluku",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214138?signature=59f291da3f31aaf5ad88b319fb0744d46dfeca47364ca2f76be7a587ce5094d9"
      },
      "Bromo":{
         "location":"Jawa Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214073?signature=6dc9c58e1437da92a0c5a78c8a5fa21a9f3a7e8d58942a76f93117fa08417438"
      },
      "Dempo":{
         "location":"Sumatera Selatan",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214089?signature=cdb75d763a7b374e75ef330c991c854d7cbe6d1f57c9c9969bf6fb235d6a1ea0"
      },
      "Dieng":{
         "location":"Jawa Tengah",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214100?signature=c17fe1d07bf99e2f2a857495f13c4cc711b6bd4f7e9832780f2508c90193c9e6"
      },
      "Dukono":{
         "location":"Maluku Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214080?signature=300ff948ff8fbfd3224f513558608e46c64adc456958167fa09a0320e1494a35"
      },
      "Gamalama":{
         "location":"Maluku Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214153?signature=82cdb741b245b6c1e74093dd5d0a04e6398057d241ba9619414bacd3c5c1ef60"
      },
      "Ibu":{
         "location":"Maluku Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214057?signature=d66a308b90b6d027685b821b02e6ae1fcbeebcf1ba45514cf46a0a2a192d0eca"
      },
      "Ijen":{
         "location":"Jawa Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214128?signature=bb5843ae677190b65dcdae2fc28b10d2e19647e716984d89676b29ee3cb829cf"
      },
      "Ili Lewotolok":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214071?signature=9dd26c093cec57d654bce17269ce3695801e178de21aaa91408ba4378c6d84e5"
      },
      "Karangetang":{
         "location":"Sulawesi Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214094?signature=c97fab70ceda897ade46205159d90b974256813080b429dfe447fa786de624ad"
      },
      "Kerinci":{
         "location":"Jambi, Sumatera Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214096?signature=92179361ee199b7aa21dec3d0691fdfb1316237c7ca2ae4596502a76965e5815"
      },
      "Lokon":{
         "location":"Sulawesi Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214084?signature=b32fe2d8ee986343f10bf5ce7d1f46503509098732aa2893421176d7328c6c0c"
      },
      "Marapi":{
         "location":"Sumatera Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214104?signature=d815a089a9def4b2e829a7d572f10b0d08a892c640225f7824640139d4b584df"
      },
      "Raung":{
         "location":"Jawa Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214092?signature=0f838bbb86a414917bc1492f84eb723ed26cca8af56b12b7662a93afa552ce0c"
      },
      "Rinjani":{
         "location":"Nusa Tenggara Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214108?signature=de6478de709bade763511e83e4a58d3339af04a0c28b361165a89659bf02da1e"
      },
      "Sangeangapi":{
         "location":"Nusa Tenggara Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214101?signature=0aceea14ae97077f8be663027acbe540f8afd44878d80dddd8c5883923ab738d"
      },
      "Sinabung":{
         "location":"Sumatera Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214090?signature=4b1e474ac8ce3cd5ef4705dc7cf61c83aeeac36e664c0bb1bd1f2e1f3769b8ec"
      },
      "Soputan":{
         "location":"Sulawesi Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214131?signature=ec21a8754ad794ebdb09c2efbe79da6744934303204b4778af2f4198bf63c6d5"
      }
   },
   "Level I (Normal)":{
      "Agung":{
         "location":"Bali",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214117?signature=d547e1a02dee6b4de79750ed289f3e50fccfdeeb2a47ded2446c88edb3a136e7"
      },
      "Ambang":{
         "location":"Sulawesi Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214130?signature=f84739326681c17601400aa51c82abad8e4881169b8607256bccf376f814e6c4"
      },
      "Anak Ranakah":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214107?signature=a368322efa5a613fcc0e5ace8c84741293c7a471b2ffc3d1fb59fe9d0dc133b5"
      },
      "Arjuno Welirang":{
         "location":"Jawa Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214133?signature=3afd8b498d89b6ce6b783b04f26b233a10bf883a1ebcc025798e1f066b164895"
      },
      "Batur":{
         "location":"Bali",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214126?signature=c6780eebf63233253bbbc23424777effcf8a0ae7252e1b65cfae5cffacea42c2"
      },
      "Batutara":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214036?signature=93c193a2bc2f1dcd1fceb0d9ce52f64812bf372aa45aecdec1a21228be5a64a3"
      },
      "Bur Ni Telong":{
         "location":"Aceh",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214113?signature=d721ac8315da393ba97a5414167c94415bc71426d0a09d6eee5236513e16f750"
      },
      "Ciremai":{
         "location":"Jawa Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214105?signature=93b8e797486d59b46490706b2b0e3c42800a675532006e2be8d2f2f2953b170f"
      },
      "Colo":{
         "location":"Sulawesi Tengah",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214098?signature=dd48190e7d7e53c4a1817d45da7c74209f0d0578cb29afac03979bf97f3e95a0"
      },
      "Ebulobo":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214083?signature=d219916c0e3bdfb40402c0f3fcaf9e6f26ad89014f31924a82d7f786fc5c1c95"
      },
      "Egon":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214088?signature=b31e62e8112ec9aa039064169f8cb1f3e3f7f6520b63b87657704c59b63f3b22"
      },
      "Galunggung":{
         "location":"Jawa Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214097?signature=01e1913eb678a5c4c4cb7e76555bfc09b7a0c918618e2bbe6fb5fd213e064d78"
      },
      "Gamkonora":{
         "location":"Maluku Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214136?signature=a94030d62729362938b70264c4e3fe8c8534c5438e3e3288e65a1d66523738cb"
      },
      "Gede":{
         "location":"Jawa Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214119?signature=bd58bd4b54086bde0688b9efdfd09c9698f091c657d68f17e3288d7ef14471b7"
      },
      "Guntur":{
         "location":"Jawa Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214095?signature=bd285f285adfc10d2fa8b8de1c8c0b598dcf0185f9ac4b60e7bbeebc4b325206"
      },
      "Ile Werung":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214115?signature=7f22d82f0e5f978ceefbefbe53ab9f4daf3cf1f964392bc337e71b846d2c98e2"
      },
      "Ili Boleng":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214079?signature=6a17eaeaef06573a9a7d7a8b6027d27b58963719c10464bb6e808b3169fccd0f"
      },
      "Inielika":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/213864?signature=1db40c333c4e9bd37f1fab0547ffdab671ccdb9eadd65b3ee37fb1304b49da6f"
      },
      "Inierie":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214141?signature=ad6159a457ee1e92c10e65cadee3d4003d88a7d313883dcc97d1464d514b192c"
      },
      "Iya":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214140?signature=d7439e06a97c91c3404aaf259ea28845619b02082ce0507fefdacb7c2548ad03"
      },
      "Kaba":{
         "location":"Bengkulu",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214099?signature=7724037ed7a1a99cfb9c3064c08671a7856cb360a765c54c58dbac075e5b1b5b"
      },
      "Kelimutu":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214134?signature=6314352ff60b6d93bc78569496a975ca5fe96dabfcdd45656e51144234809e68"
      },
      "Kelud":{
         "location":"Jawa Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214120?signature=45c568efe9c3da45791653a38c7a3ea97fe698c88048c331c3d9e88f33c75d66"
      },
      "Kie Besi":{
         "location":"Maluku Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214146?signature=1cbf07e7339196401383da7adcec57e9e57f5792a5380a0b054f3061504015bc"
      },
      "Lamongan":{
         "location":"Jawa Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214111?signature=c9e5086ea9a6facbcf8649680b9763c8d1668fa1c2b57cf0463882926fae9ddf"
      },
      "Lereboleng":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214114?signature=5d91925617e6ae2e57724e41089472cc13f1b043fb092c33c3a5fbe859ba436e"
      },
      "Lewotobi Laki-laki":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214121?signature=33e22f1596528aee9152a6461a49ff6825fefb6477ec0c2ba3be67c3c7294adf"
      },
      "Lewotobi Perempuan":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214129?signature=d315cbb112543887ade8230eba0e892aed8f91fe1db8072acc34581a62f4f3c9"
      },
      "Mahawu":{
         "location":"Sulawesi Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214086?signature=9bba5e6e5280cfdca75dc2d899327a695094a909385d254bf1184fb58b73365e"
      },
      "Papandayan":{
         "location":"Jawa Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214122?signature=65ea0f3ef39e9eaaf60d532eea22529cdfbf80414d9167db7d82350638d39307"
      },
      "Peut Sague":{
         "location":"Daerah Istimewa Aceh",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214124?signature=e1da786750d7466230fa9f182d0d84ff933a06669250d620af0441fbcf19c0fa"
      },
      "Rokatenda":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214116?signature=6776a67eb8f777f45213a1b03d04515cbc24cf2d9f2d04aa8cc0f483e20f55e7"
      },
      "Ruang":{
         "location":"Sulawesi Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214106?signature=65ed78c89255d92242a542f132d72e67bc99c0510912d28896882ce4e4248fc1"
      },
      "Salak":{
         "location":"Jawa Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214093?signature=9b6e319399f7d3703c778ee592b4af633ba11d002140e8a03e7f09dfdeb98081"
      },
      "Seulawah Agam":{
         "location":"Daerah Istimewa Aceh",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214139?signature=ba6cb2070c44be5f8da73f3a01b8196b1745d80692c0d2c5008d6ed496a59b63"
      },
      "Sirung":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214145?signature=d25ee9451a8fdb28382765bd87eefa75e6f14e22948565a23e47ec4966c2d5a5"
      },
      "Slamet":{
         "location":"Jawa Tengah",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214081?signature=011eda7c455708aa64b2bd9753b38502fe1741b0f85c602f3d56bf967ab2684f"
      },
      "Sorikmarapi":{
         "location":"Sumatera Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214110?signature=4cafad392837db407f9e8b4e302e4787725b25d2289e2ff443a47b892945723b"
      },
      "Sumbing":{
         "location":"Jawa Tengah",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214137?signature=e2bf32b5c31e5b377a7d9621606a2f09c6dcaa24e10a565d3c885fdc27ad88d0"
      },
      "Sundoro":{
         "location":"Jawa Tengah",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214123?signature=7ed7253a37f3687fa1c4a9de7f9082efa51cdf2f42507a15cb03422c04d701df"
      },
      "Talang":{
         "location":"Sumatera Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214102?signature=0762bfdaa71b4037917ff1567b03382ca5bd1cb4f5413c7d2b49b31b584df7dd"
      },
      "Tambora":{
         "location":"Nusa Tenggara Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214127?signature=9dbc35213abf4260be07ca8c7d0aad103a36b480be156c61a8bef14df8e5338a"
      },
      "Tandikat":{
         "location":"Sumatera Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214103?signature=220f5935487f3739dbc7938c28d4ac481da60d6e1c107acefd65de30b0a487dc"
      },
      "Tangkoko":{
         "location":"Sulawesi Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214109?signature=40598c02bf3d13c9fd9916f259595f5e8fe5a7ee3eba8edc7b427284ab109166"
      },
      "Tangkuban Parahu":{
         "location":"Jawa Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214125?signature=5d7cee319d0b8863fcee3fe17cd12a7fca22936010b389729271d30150aa4efc"
      },
      "Wurlali":{
         "location":"Maluku",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214118?signature=c38255516d8089729183534bf2ef40d97bdd80e7885a7563b2ab83af297e58ff"
      }
   }
}
```
## Eruption 
To get information about the eruption, you can use the code below

```python
import Magma
print(Magma.magmaeruption())
```

The output will look like this:
```json
{
   "10-08-2024":{
      "WIB":{
         "09:57":{
            "volcano_name":"Semeru",
            "author":"Liswanto, A.P.",
            "information":"Terjadi erupsi G. Semeru pada hari Selasa, 08 Oktober 2024, pukul 09:57 WIB. Visual letusan tidak teramati.\n\nSaat laporan ini dibuat, erupsi masih berlangsung.",
            "image":"",
            "detail":"https://magma.esdm.go.id/v1/gunung-api/informasi-letusan/ee67e951-8520-11ef-8afe-005056b54356/show"
         },
         "09:40":{
            "volcano_name":"Semeru",
            "author":"Liswanto, A.P.",
            "information":"Terjadi erupsi G. Semeru pada hari Selasa, 08 Oktober 2024, pukul 09:40 WIB. Visual letusan tidak teramati.\n\nSaat laporan ini dibuat, erupsi masih berlangsung.",
            "image":"",
            "detail":"https://magma.esdm.go.id/v1/gunung-api/informasi-letusan/897b4ef2-851e-11ef-8afe-005056b54356/show"
         },
         "08:13":{
            "volcano_name":"Semeru",
            "author":"Liswanto, A.P.",
            "information":"Terjadi erupsi G. Semeru pada hari Selasa, 08 Oktober 2024, pukul 08:13 WIB. Visual letusan tidak teramati.\n\nSaat laporan ini dibuat, erupsi masih berlangsung.",
            "image":"",
            "detail":"https://magma.esdm.go.id/v1/gunung-api/informasi-letusan/51c434ae-8512-11ef-8afe-005056b54356/show"
         },
         "08:09":{
            "volcano_name":"Semeru",
            "author":"Liswanto, A.P.",
            "information":"Terjadi erupsi G. Semeru pada hari Selasa, 08 Oktober 2024, pukul 08:09 WIB. Visual letusan tidak teramati.\n\nSaat laporan ini dibuat, erupsi masih berlangsung.",
            "image":"",
            "detail":"https://magma.esdm.go.id/v1/gunung-api/informasi-letusan/d95f366e-8511-11ef-8afe-005056b54356/show"
         }
      }
   },
   "10-07-2024":{
      "WITA":{
         "17:52":{
            "volcano_name":"Lewotobi Laki-laki",
            "author":"Emanuel Rofinus Bere, A.Md.Kom.",
            "information":"Terjadi erupsi G. Lewotobi Laki-laki pada hari Senin, 07 Oktober 2024, pukul 17:52 WITA dengan tinggi kolom abu teramati ± 1000 m di atas puncak (± 2584 m di atas permukaan laut). Kolom abu teramati berwarna kelabu dengan intensitas tebal ke arah barat dan barat laut.\n\nErupsi ini terekam di seismograf dengan amplitudo maksimum 7.4 mm dan durasi 653 detik.",
            "image":"https://magma.vsi.esdm.go.id/img/crs/VEN_LWK20241007171319.png",
            "detail":"https://magma.esdm.go.id/v1/gunung-api/informasi-letusan/c6f57e4b-8494-11ef-8afe-005056b54356/show"
         },
         "12:15":{
            "volcano_name":"Lewotobi Laki-laki",
            "author":"Yohanes Kolli Sorywutun, A.Md.",
            "information":"Terjadi erupsi G. Lewotobi Laki-laki pada hari Senin, 07 Oktober 2024, pukul 12:15 WITA dengan tinggi kolom abu teramati ± 1000 m di atas puncak (± 2584 m di atas permukaan laut). Kolom abu teramati berwarna kelabu dengan intensitas tebal ke arah barat daya.\n\nSaat laporan ini dibuat, erupsi masih berlangsung.",
            "image":"https://magma.vsi.esdm.go.id/img/crs/VEN_LWK20241007112402.png",
            "detail":"https://magma.esdm.go.id/v1/gunung-api/informasi-letusan/fb7c6070-8463-11ef-8afe-005056b54356/show"
         },
         "11:35":{
            "volcano_name":"Lewotobi Laki-laki",
            "author":"Yohanes Kolli Sorywutun, A.Md.",
            "information":"Terjadi erupsi G. Lewotobi Laki-laki pada hari Senin, 07 Oktober 2024, pukul 11:35 WITA dengan tinggi kolom abu teramati ± 700 m di atas puncak (± 2284 m di atas permukaan laut). Kolom abu teramati berwarna kelabu dengan intensitas tebal ke arah barat daya.\n\nErupsi ini terekam di seismograf dengan amplitudo maksimum 5.1 mm dan durasi 790 detik.",
            "image":"https://magma.vsi.esdm.go.id/img/crs/VEN_LWK20241007105159.png",
            "detail":"https://magma.esdm.go.id/v1/gunung-api/informasi-letusan/80e90af8-845f-11ef-8afe-005056b54356/show"
         },
         "05:03":{
            "volcano_name":"Lewotobi Laki-laki",
            "author":"Emanuel Rofinus Bere, A.Md.Kom.",
            "information":"Terjadi erupsi G. Lewotobi Laki-laki pada hari Senin, 07 Oktober 2024, pukul 05:03 WITA dengan tinggi kolom abu teramati ± 800 m di atas puncak (± 2384 m di atas permukaan laut). Kolom abu teramati berwarna kelabu dengan intensitas tebal ke arah barat daya.\n\nErupsi ini terekam di seismograf dengan amplitudo maksimum 4.4 mm dan durasi 279 detik.",
            "image":"https://magma.vsi.esdm.go.id/img/crs/VEN_LWK20241007041144.png",
            "detail":"https://magma.esdm.go.id/v1/gunung-api/informasi-letusan/974d805d-8427-11ef-8afe-005056b54356/show"
         },
         "00:56":{
            "volcano_name":"Lewotobi Laki-laki",
            "author":"Emanuel Rofinus Bere, A.Md.Kom.",
            "information":"Terjadi erupsi G. Lewotobi Laki-laki pada hari Senin, 07 Oktober 2024, pukul 00:56 WITA dengan tinggi kolom abu teramati ± 800 m di atas puncak (± 2384 m di atas permukaan laut). Kolom abu teramati berwarna kelabu dengan intensitas tebal ke arah barat daya.\n\nErupsi ini terekam di seismograf dengan amplitudo maksimum 7.4 mm dan durasi 172 detik.",
            "image":"https://magma.vsi.esdm.go.id/img/crs/VEN_LWK20241007000306.png",
            "detail":"https://magma.esdm.go.id/v1/gunung-api/informasi-letusan/db2a7a1f-8404-11ef-8afe-005056b54356/show"
         }
      },
      "WIT":{
         "11:48":{
            "volcano_name":"Ibu",
            "author":"Rivaldi Hasan",
            "information":"Terjadi erupsi G. Ibu pada hari Senin, 07 Oktober 2024, pukul 11:48 WIT. Visual letusan tidak teramati.\n\nErupsi ini terekam di seismograf dengan amplitudo maksimum 18 mm dan durasi 45 detik.",
            "image":"https://magma.vsi.esdm.go.id/img/crs/VEN_IBU20241007095446.png",
            "detail":"https://magma.esdm.go.id/v1/gunung-api/informasi-letusan/831f4722-8457-11ef-8afe-005056b54356/show"
         }
      },
      "WIB":{
         "09:19":{
            "volcano_name":"Semeru",
            "author":"Ghufron Alwi",
            "information":"Terjadi erupsi G. Semeru pada hari Senin, 07 Oktober 2024, pukul 09:19 WIB. Visual letusan tidak teramati.\n\nErupsi ini terekam di seismograf dengan amplitudo maksimum 22 mm dan durasi 100 detik.",
            "image":"",
            "detail":"https://magma.esdm.go.id/v1/gunung-api/informasi-letusan/ac3a89f2-8452-11ef-8afe-005056b54356/show"
         },
         "07:40":{
            "volcano_name":"Semeru",
            "author":"Ghufron Alwi",
            "information":"Terjadi erupsi G. Semeru pada hari Senin, 07 Oktober 2024, pukul 07:40 WIB. Visual letusan tidak teramati.\n\nErupsi ini terekam di seismograf dengan amplitudo maksimum 23 mm dan durasi 120 detik.",
            "image":"",
            "detail":"https://magma.esdm.go.id/v1/gunung-api/informasi-letusan/fba99d45-8444-11ef-8afe-005056b54356/show"
         }
      }
   },
   "10-06-2024":{
      "WIB":{
         "16:40":{
            "volcano_name":"Semeru",
            "author":"Ghufron Alwi",
            "information":"Terjadi erupsi G. Semeru pada hari Minggu, 06 Oktober 2024, pukul 16:40 WIB. Visual letusan tidak teramati.\n\nErupsi ini terekam di seismograf dengan amplitudo maksimum 22 mm dan durasi 112 detik.",
            "image":"",
            "detail":"https://magma.esdm.go.id/v1/gunung-api/informasi-letusan/3c9c368d-83c7-11ef-8afe-005056b54356/show"
         },
         "14:59":{
            "volcano_name":"Semeru",
            "author":"Ghufron Alwi",
            "information":"Terjadi erupsi G. Semeru pada hari Minggu, 06 Oktober 2024, pukul 14:59 WIB. Visual letusan tidak teramati.\n\nErupsi ini terekam di seismograf dengan amplitudo maksimum 22 mm dan durasi 93 detik.",
            "image":"",
            "detail":"https://magma.esdm.go.id/v1/gunung-api/informasi-letusan/03029c71-83b9-11ef-8afe-005056b54356/show"
         },
         "13:49":{
            "volcano_name":"Semeru",
            "author":"Ghufron Alwi",
            "information":"Terjadi erupsi G. Semeru pada hari Minggu, 06 Oktober 2024, pukul 13:49 WIB. Visual letusan tidak teramati.\n\nErupsi ini terekam di seismograf dengan amplitudo maksimum 22 mm dan durasi 122 detik.",
            "image":"",
            "detail":"https://magma.esdm.go.id/v1/gunung-api/informasi-letusan/2ff660e3-83af-11ef-8afe-005056b54356/show"
         }
      }
   }
}
```

## Level + Other Information
This code will show you the level of the volcano, the website link and other info (such as date, recommendation, volcano info, and etc). It'll take about 1 minute to get the information (depending on internet and device)

```python
import Magma
print(Magma.magmaeruption())
```

The output will look like this:
```json
{
   "Level IV (Awas)":{
      
   },
   "Level III (Siaga)":{
      "Anak Krakatau":{
         "location":"Lampung",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214150?signature=7938285319e0301c283407938f5b6bf7d3b74139dbea51c08ca3f17c8e2a7234",
         "detail":{
            "title":"Anak Krakatau, Jumat - 03 Februari 2023, periode 12:00-18:00 WIB",
            "author":" Deny Mardiono",
            "location":"Gunung Api Anak Krakatau terletak di Kab\\Kota Lampung Selatan, Lampung dengan posisi geografis di Latitude -6.102°LU, Longitude 105.423°BT dan memiliki ketinggian 157 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/KRA/KRA202302031200.png",
            "visual_observation":"Gunung api terlihat jelas. Teramati asap kawah utama berwarna putih dengan intensitas tipis hingga sedang tinggi sekitar 50-150 meter dari puncak. Cuaca berawan, angin lemah ke arah timur.",
            "other_description":"Ombak laut tenang.",
            "climatology":"KlimatologiCuaca berawan, angin lemah ke arah timur. Suhu udara sekitar 27.7-28.6°C. Kelembaban 50-51%.",
            "seismic_observation":"Pengamatan Kegempaan12 kali Harmonik dengan amplitudo 26-48 mm, dan lama gempa 25-324 detik.1 kali gempa Tremor Menerus dengan amplitudo 3-45 mm, dominan 25 mm.",
            "recommendation":"RekomendasiMasyarakat/pengunjung/wisatawan/pendaki tidak mendekati G. Anak Krakatau atau beraktivitas dalam radius 5 km dari kawah aktif."
         }
      },
      "Merapi":{
         "location":"Daerah Istimewa Yogyakarta dan Jawa Tengah",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214152?signature=eb7e4dc8a452d8945fdcf6d52062c102587b8409b98ba4691696a9f3db996342",
         "detail":{
            "title":"Merapi, Jumat - 03 Februari 2023, periode 12:00-18:00 WIB",
            "author":" Triyono",
            "location":"Gunung Api Merapi terletak di Kab\\Kota Sleman, Magelang, Boyolali, Klaten, Daerah Istimewa Yogyakarta dan Jawa Tengah dengan posisi geografis di Latitude -7.542°LU, Longitude 110.442°BT dan memiliki ketinggian 2968 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/MER/MER202302031200.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca berawan hingga mendung, angin lemah ke arah timur.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga mendung, angin lemah ke arah timur. Suhu udara sekitar 17-22°C. Kelembaban 69-91.6%. Tekanan udara 624.75-690.15 mmHg.",
            "seismic_observation":"Pengamatan Kegempaan6 kali gempa Guguran dengan amplitudo 3-9 mm dan lama gempa 43.9-103 detik.22 kali gempa Vulkanik Dalam dengan amplitudo 8-16 mm, S-P 0.6-0.9 detik dan lama gempa 7.5-10.5 detik.",
            "recommendation":"Rekomendasi1. Potensi bahaya saat ini berupa guguran lava dan awanpanas pada sektor selatan-barat daya meliputi Sungai Boyong sejauh maksimal 5 km, Sungai Bedog, Krasak, Bebeng sejauh maksimal 7 km. Pada sektor tenggara meliputi Sungai Woro sejauh maksimal 3 km dan Sungai Gendol 5 km. Sedangkan lontaran material vulkanik bila terjadi letusan eksplosif dapat menjangkau radius 3 km dari puncak.2. Masyarakat agar tidak melakukan kegiatan apapun di daerah potensi bahaya.3. Masyarakat agar mengantisipasi gangguan akibat abu vulkanik dari erupsi Gunung Merapi serta mewaspadai bahaya lahar terutama saat terjadi hujan di seputar G. Merapi.4. Jika terjadi perubahan aktivitas yang signifikan, maka status aktivitas Gunung Merapi akan segera ditinjau kembali."
         }
      },
      "Semeru":{
         "location":"Jawa Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214151?signature=f3d92693bbeaf428ea5131e3acf29cc9f2c60a8499353e6d0244b6648908290e",
         "detail":{
            "title":"Semeru, Jumat - 03 Februari 2023, periode 12:00-18:00 WIB",
            "author":" Mukdas Sofian",
            "location":"Gunung Api Semeru terletak di Kab\\Kota Lumajang, Malang, Jawa Timur dengan posisi geografis di Latitude -8.108°LU, Longitude 112.92°BT dan memiliki ketinggian 3676 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/SMR/SMR202302031200.png",
            "visual_observation":"Gunung api tertutup Kabut 0-I hingga tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca berawan hingga mendung, angin lemah ke arah barat daya.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga mendung, angin lemah ke arah barat daya. Suhu udara sekitar 24-26°C.",
            "seismic_observation":"Pengamatan Kegempaan25 kali gempa Letusan/Erupsi dengan amplitudo 15-22 mm, dan lama gempa 40-120 detik.5 kali gempa Tektonik Jauh dengan amplitudo 15-36 mm, S-P 16-56 detik dan lama gempa 60-100 detik.",
            "recommendation":"Rekomendasi1. Tidak melakukan aktivitas apapun di sektor tenggara di sepanjang Besuk Kobokan, sejauh 13  km dari puncak (pusat erupsi). Di luar jarak tersebut, masyarakat tidak melakukan aktivitas pada jarak 500 meter dari tepi sungai (sempadan sungai) di sepanjang Besuk Kobokan karena berpotensi terlanda perluasan awan panas dan aliran lahar hingga jarak 17 km dari puncak.2. Tidak beraktivitas dalam radius 5  Km dari kawah/puncak Gunung Api Semeru karena rawan terhadap bahaya lontaran batu (pijar).3. Mewaspadai potensi awan panas guguran (APG), guguran lava, dan lahar di sepanjang aliran sungai/lembah yang berhulu di puncak Gunung Api Semeru, terutama sepanjang Besuk Kobokan, Besuk Bang, Besuk Kembar, dan Besuk Sat serta potensi lahar pada sungai-sungai kecil yang merupakan anak sungai dari Besuk Kobokan."
         }
      }
   },
   "Level II (Waspada)":{
      "Awu":{
         "location":"Sulawesi Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214070?signature=6e72308ad15a889976904bb08e35b4b1d57e8e75e80021000fdf8601bb01c59d",
         "detail":{
            "title":"Awu, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Tommy Luhut Marbun",
            "location":"Gunung Api Awu terletak di Kab\\Kota Kepulauan Sangihe, Sulawesi Utara dengan posisi geografis di Latitude 3.682846°LU, Longitude 125.45598°BT dan memiliki ketinggian 1320 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/AWU/AWU202302022400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-I hingga tertutup Kabut 0-II. Asap kawah tidak teramati. Cuaca berawan hingga hujan, angin lemah ke arah barat daya.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah ke arah barat daya. Suhu udara sekitar 25-32°C. Kelembaban 66-70%. Intensitas curah hujan 6.7 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan1 kali Tremor Non-Harmonik dengan amplitudo 4 mm, dan lama gempa 155 detik.3 kali gempa Vulkanik Dangkal dengan amplitudo 8-21 mm, dan lama gempa 9-15 detik.7 kali gempa Vulkanik Dalam dengan amplitudo 7-20 mm, S-P 1-1.5 detik dan lama gempa 9-18 detik.20 kali gempa Tektonik Jauh dengan amplitudo 4-20 mm, S-P 12-20 detik dan lama gempa 40-193 detik.",
            "recommendation":"Rekomendasi1. Masyarakat dan pengunjung/wisatawan agar tidak mendekati dan beraktivitas di dalam radius 3 kilometer dari kawah puncak G. Awu.2. Masyarakat di sekitar G. Awu diharap tetap tenang, tidak terpancing isu-isu mengenai aktivitas G. Awu yang tidak dapat dipertanggungjawabkan kebenarannya. Masyarakat harap mengikuti arahan dari Badan Penanggulangan Bencana Daerah Kabupaten Kepulauan Sangihe.3. Masyarakat maupun Pemerintah Daerah dan instansi terkait lainnya dapat memantau perkembangan tingkat aktivitas maupun rekomendasi G. Awu setiap saat melalui aplikasi MAGMA Indonesia yang dapat diakses melalui website https://magma.esdm.go.id atau melalui aplikasi android MAGMA Indonesia yang dapat diunduh di Google Play."
         }
      },
      "Banda Api":{
         "location":"Maluku",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214138?signature=59f291da3f31aaf5ad88b319fb0744d46dfeca47364ca2f76be7a587ce5094d9",
         "detail":{
            "title":"Banda Api, Kamis - 02 Februari 2023, periode 00:00-24:00 WIT",
            "author":" Wahyu Wijayanto",
            "location":"Gunung Api Banda Api terletak di Kab\\Kota Maluku Tengah, Maluku dengan posisi geografis di Latitude -4.523°LU, Longitude 129.881°BT dan memiliki ketinggian 641 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/BAN/BAN202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-I. Teramati asap kawah utama berwarna putih dengan intensitas tipis tinggi sekitar 20-22 meter dari puncak. Cuaca berawan hingga mendung, angin lemah hingga sedang ke arah timur.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga mendung, angin lemah hingga sedang ke arah timur. Suhu udara sekitar 29-32°C.",
            "seismic_observation":"Pengamatan Kegempaan3 kali gempa Vulkanik Dalam dengan amplitudo 7-11 mm, S-P 0.81-1.92 detik dan lama gempa 7.87-17.1 detik.3 kali gempa Tektonik Jauh dengan amplitudo 10-15 mm, S-P tidak teramati dan lama gempa 43.82-175.08 detik.",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Banda Api dan pengunjung/wisatawan agar tidak beraktivitas di dalam radius 1 km dari kawah G. Banda Api."
         }
      },
      "Bromo":{
         "location":"Jawa Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214073?signature=6dc9c58e1437da92a0c5a78c8a5fa21a9f3a7e8d58942a76f93117fa08417438",
         "detail":{
            "title":"Bromo, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Wahyu Andrian Kusuma",
            "location":"Gunung Api Bromo terletak di Kab\\Kota Probolinggo, Jawa Timur dengan posisi geografis di Latitude -7.942°LU, Longitude 112.95°BT dan memiliki ketinggian 2329 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/BRO/BRO202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Teramati asap kawah utama berwarna putih dengan intensitas tipis, sedang hingga tebal tinggi sekitar 50-300 meter dari puncak. Cuaca berawan hingga hujan, angin lemah hingga kencang ke arah timur laut dan timur.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah hingga kencang ke arah timur laut dan timur. Suhu udara sekitar 12-19°C. Intensitas curah hujan 5.6 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Tremor Menerus dengan amplitudo 0.5-1 mm, dominan 0.5 mm.",
            "recommendation":"Rekomendasi1. Masyarakat di sekitar G. Bromo dan pengunjung/wisatawan/ pendaki tidak memasuki kawasan dalam radius 1 km dari kawah aktif G. Bromo.2. Masyarakat di sekitar G. Bromo, pedagang, wisatawan, pendaki, dan pengelola wisata G. Bromo agar mewaspadai terjadinya letusan freatik yang bersifat tiba - tiba dan tanpa didahului oleh gejala-gejala vulkanik yang jelas."
         }
      },
      "Dempo":{
         "location":"Sumatera Selatan",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214089?signature=cdb75d763a7b374e75ef330c991c854d7cbe6d1f57c9c9969bf6fb235d6a1ea0",
         "detail":{
            "title":"Dempo, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Ardi",
            "location":"Gunung Api Dempo terletak di Kab\\Kota Lahat, Empat Lawang, Kota Pagar Alam, Sumatera Selatan dengan posisi geografis di Latitude -4.03°LU, Longitude 103.13°BT dan memiliki ketinggian 3173 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/DEM/DEM202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Asap kawah nihil. Cuaca berawan hingga mendung, angin lemah hingga sedang ke arah timur dan selatan.",
            "other_description":"Terekam noise",
            "climatology":"KlimatologiCuaca berawan hingga mendung, angin lemah hingga sedang ke arah timur dan selatan. Suhu udara sekitar 18-27°C.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Tektonik Jauh dengan amplitudo 30 mm, S-P 22 detik dan lama gempa 192 detik.1 kali gempa Tremor Menerus dengan amplitudo 0.5-1 mm, dominan 0.5 mm.",
            "recommendation":"RekomendasiAgar masyarakat, pengunjung/wisatawan tidak mendekati dan bermalam (camping) di pusat aktivitas kawah Marapi - G. Dempo dalam radius 1 km, serta arah bukaan kawah sejauh 2 km ke sektor utara, mengingat kawah sebagai pusat letusan dan gas-gas vulkanik yang dapat membahayakan bagi kehidupan."
         }
      },
      "Dieng":{
         "location":"Jawa Tengah",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214100?signature=c17fe1d07bf99e2f2a857495f13c4cc711b6bd4f7e9832780f2508c90193c9e6",
         "detail":{
            "title":"Dieng, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Surip",
            "location":"Gunung Api Dieng terletak di Kab\\Kota Banjarnegara, Wonosobo, Batang, Jawa Tengah dengan posisi geografis di Latitude -7.2°LU, Longitude 109.92°BT dan memiliki ketinggian 2565 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/DIE/DIE202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-II. Teramati asap kawah utama berwarna putih dengan intensitas tipis hingga tebal tinggi sekitar 10-30 meter dari puncak. Cuaca cerah hingga mendung, angin kencang ke arah timur.",
            "other_description":"Suhu Kawah Sileri\nMin 67.9°C, Max 68.8° C,  rata-rata 68.3°C.\nSuhu Tanah Kawah Sileri\nMin 22. 1°C, Max 22.9 ° C,  rata-rata 22.4°C.\nKonsentrasi CO2 Kawah Timbang. \nMin 0.15%Vol, Max 0.17%Vol,  rata-rata 0.16%Vol.\nKonsentrasi CO2 Kawah Sikendang. \nMin 0.123%Vol, Max 0.138%Vol,  rata-rata 0.127%Vol.",
            "climatology":"KlimatologiCuaca cerah hingga mendung, angin kencang ke arah timur. Suhu udara sekitar 12-20°C.",
            "seismic_observation":"Pengamatan Kegempaan23 kali gempa Tektonik Lokal dengan amplitudo 10.7-42.7 mm, S-P 0.28-2.42 detik dan lama gempa 5.35-16.75 detik.1 kali gempa Tektonik Jauh dengan amplitudo 21.4 mm, S-P tidak teramati dan lama gempa 48.88 detik.",
            "recommendation":"Rekomendasi1. Masyarakat dan wisatawan tidakmendekati Kawah Sileri pada jarak 1km meter dari bibir kawah.2.Masyarakat tidak mendekati kawasansektor barat daya, selatan dantenggara Kawah Timbang dalam jarak500 meter agar terhindar dari alirangas CO2 yang sangat berbahaya bagikehidupan dan agar waspada jikamelakukan penggalian tanah di sekitarKawah Timbang karena dapatberpotensi terpapar gas CO2 yangberbahaya bagi kehidupan.3.Masyarakat dan wisatawan agar tidakmemasuki kawah-kawah di KomplekDieng yang dapat berpotensi terjadierupsi freatik berupa semburanlumpur atau lontaran material; dan dandi kawah-kawah dengan konsentrasigas vulkanik yang tinggi danberbahaya bagi kehidupan.4.Pemerintah Daerah, BPBD Provinsi danKabupaten agar senantiasaberkoordinasi dengan PosPengamatan Gunung Api Dieng diDesa Karang Tengah, KecamatanBatur, Kabupaten Banjarnegara, Telp.085326951587 atau Pusat Vulkanologidan MItigasi Bencana Geologi\\x02 BadanGeologi."
         }
      },
      "Dukono":{
         "location":"Maluku Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214080?signature=300ff948ff8fbfd3224f513558608e46c64adc456958167fa09a0320e1494a35",
         "detail":{
            "title":"Dukono, Kamis - 02 Februari 2023, periode 00:00-24:00 WIT",
            "author":" Bambang Sugiono",
            "location":"Gunung Api Dukono terletak di Kab\\Kota Halmahera Utara, Maluku Utara dengan posisi geografis di Latitude 1.693°LU, Longitude 127.894°BT dan memiliki ketinggian 1229 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/DUK/DUK202302022400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-I hingga tertutup Kabut 0-III. Asap kawah nihil. Cuaca berawan hingga hujan, angin lemah hingga sedang ke arah selatan.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah hingga sedang ke arah selatan. Suhu udara sekitar 26.5-29°C. Kelembaban 82-83%.",
            "seismic_observation":"Pengamatan Kegempaan3 kali gempa Tektonik Jauh dengan amplitudo 7-34 mm, S-P 17.41-20.21 detik dan lama gempa 52.22-61.585 detik.1 kali gempa Tremor Menerus dengan amplitudo 0.5-2 mm, dominan 1 mm.",
            "recommendation":"Rekomendasi(1)Masyarakat di sekitar G. Dukono dan pengunjung/wisatawan agar tidak beraktivitas, mendaki, dan mendekati Kawah Malupang Warirang di dalam radius 2 km.(2)Mengingat letusan dengan abu vulkanik secara periodik terjadi dan sebaran abu mengikuti arah dan kecepatan angin, sehingga area landaan abunya tidak tetap, maka direkomendasikan agar masyarakat di sekitar G. Dukono untuk selalu menyediakan masker/penutup hidung dan mulut untuk digunakan pada saat dibutuhkan guna menghindari ancaman bahaya abu vulkanik pada sistem pernafasan."
         }
      },
      "Gamalama":{
         "location":"Maluku Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214153?signature=82cdb741b245b6c1e74093dd5d0a04e6398057d241ba9619414bacd3c5c1ef60",
         "detail":{
            "title":"Gamalama, Jumat - 03 Februari 2023, periode 00:00-24:00 WIT",
            "author":" Iwan Amat",
            "location":"Gunung Api Gamalama terletak di Kab\\Kota Ternate, Maluku Utara dengan posisi geografis di Latitude 0.8°LU, Longitude 127.33°BT dan memiliki ketinggian 1715 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/GML/GML202302032400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-I hingga tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca berawan hingga hujan, angin lemah hingga kencang ke arah tenggara dan selatan.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah hingga kencang ke arah tenggara dan selatan. Suhu udara sekitar 24-30°C. Kelembaban 76-91%. Intensitas curah hujan 2.5 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Vulkanik Dalam dengan amplitudo 3 mm, S-P 1.68 detik dan lama gempa 16.62 detik.2 kali gempa Tektonik Lokal dengan amplitudo 2-5 mm, S-P 7.91-9.04 detik dan lama gempa 20.71-31.02 detik.6 kali gempa Tektonik Jauh dengan amplitudo 8-44 mm, S-P 12.28-33.97 detik dan lama gempa 30.29-95.81 detik.",
            "recommendation":"Rekomendasi(1) Masyarakat di sekitar G.Gamalama dan pengunjung/wisatawan agar tidak beraktivitas di dalam radius 1.5 km dari kawah puncak G.Gamalama(2) Pada musim hujan, masyarakat yang tinggal di sekitar aliran sungai yang berhulu di G. Gamalama agar mewaspadai potensi ancaman bahaya sekunder berupa aliran lahar."
         }
      },
      "Ibu":{
         "location":"Maluku Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214057?signature=d66a308b90b6d027685b821b02e6ae1fcbeebcf1ba45514cf46a0a2a192d0eca",
         "detail":{
            "title":"Ibu, Rabu - 01 Februari 2023, periode 00:00-24:00 WIT",
            "author":" Axl Roeroe",
            "location":"Gunung Api Ibu terletak di Kab\\Kota Halmahera Barat, Maluku Utara dengan posisi geografis di Latitude 1.488°LU, Longitude 127.63°BT dan memiliki ketinggian 1325 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/IBU/IBU202302012400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-I hingga tertutup Kabut 0-III. Teramati asap kawah utama berwarna putih dan kelabu dengan intensitas tipis, sedang hingga tebal tinggi sekitar 200-600 meter dari puncak. Cuaca berawan hingga hujan, angin lemah hingga sedang ke arah barat daya dan barat.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah hingga sedang ke arah barat daya dan barat.",
            "seismic_observation":"Pengamatan Kegempaan85 kali gempa Letusan/Erupsi dengan amplitudo 15-28 mm, dan lama gempa 20-75 detik.33 kali gempa Hembusan dengan amplitudo 5-14 mm, dan lama gempa 15-50 detik.7 kali Harmonik dengan amplitudo 3-7 mm, dan lama gempa 30-80 detik.74 kali gempa Vulkanik Dangkal dengan amplitudo 2-6 mm, dan lama gempa 5-12 detik.30 kali gempa Tektonik Jauh dengan amplitudo 2-31 mm, S-P tidak teramati dan lama gempa 30-310 detik.",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Ibu dan pengunjung/ wisatawan agar tidak beraktivitas di dalam radius 2,0 km dan perluasan sektoral berjarak 3,5 km ke arah bukaan kawah di bagian utara dari kawah aktif G. Ibu.Jika terjadi hujan abu, masyarakat yang beraktivitas diluar rumah disarankan untuk menggunakan pelindung hidung, mulut (masker) dan mata (kacamata)."
         }
      },
      "Ijen":{
         "location":"Jawa Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214128?signature=bb5843ae677190b65dcdae2fc28b10d2e19647e716984d89676b29ee3cb829cf",
         "detail":{
            "title":"Ijen, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Agung Tri Subekti",
            "location":"Gunung Api Ijen terletak di Kab\\Kota Banyuwangi, Bondowoso, Jawa Timur dengan posisi geografis di Latitude -8.058°LU, Longitude 114.242°BT dan memiliki ketinggian 2386 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/IJE/IJE202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Teramati asap kawah utama berwarna putih dengan intensitas tipis tinggi sekitar 50-100 meter dari puncak. Cuaca berawan hingga hujan, angin lemah ke arah timur dan barat.",
            "other_description":"1.  Waspadai potensi keluarnya gas berbahaya dari danau kawah; \n2. Waspadai potensi longsor pada dinding kawah.",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah ke arah timur dan barat. Suhu udara sekitar 21-27°C. Kelembaban 76-90%.",
            "seismic_observation":"Pengamatan Kegempaan18 kali gempa Hembusan dengan amplitudo 2-8 mm, dan lama gempa 20-40 detik.20 kali gempa Vulkanik Dangkal dengan amplitudo 2-6 mm, dan lama gempa 7-18 detik.2 kali gempa Vulkanik Dalam dengan amplitudo 5-44 mm, S-P 1-1.47 detik dan lama gempa 11-19 detik.3 kali gempa Tektonik Jauh dengan amplitudo 2-30 mm, S-P 14-28 detik dan lama gempa 43-65 detik.1 kali gempa Tremor Menerus dengan amplitudo 0.5-2 mm, dominan 1 mm.",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Ijen dan pengunjung/wisatawan/penambang agar tidak mendekati kawah dalam radius 1.5 km dari bibir kawah"
         }
      },
      "Ili Lewotolok":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214071?signature=9dd26c093cec57d654bce17269ce3695801e178de21aaa91408ba4378c6d84e5",
         "detail":{
            "title":"Ili Lewotolok, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Yeremias Kristianto Pugel",
            "location":"Gunung Api Ili Lewotolok terletak di Kab\\Kota Lembata, Nusa Tenggara Timur dengan posisi geografis di Latitude -8.272°LU, Longitude 123.505°BT dan memiliki ketinggian 1423 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/LEW/LEW202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-II. Teramati asap kawah utama berwarna putih dengan intensitas sedang hingga tebal tinggi sekitar 10-25 meter dari puncak. Cuaca cerah hingga berawan, angin lemah hingga sedang ke arah timur dan tenggara.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca cerah hingga berawan, angin lemah hingga sedang ke arah timur dan tenggara. Suhu udara sekitar 26.4-31°C. Kelembaban 72-82%.",
            "seismic_observation":"Pengamatan Kegempaan2 kali gempa Letusan/Erupsi dengan amplitudo 8.3-18.2 mm, dan lama gempa 44-61 detik.43 kali gempa Hembusan dengan amplitudo 1.5-36.7 mm, dan lama gempa 15-48 detik.1 kali gempa Vulkanik Dalam dengan amplitudo 17.6 mm, S-P 0.7 detik dan lama gempa 15 detik.2 kali gempa Tektonik Jauh dengan amplitudo 1-6.9 mm, S-P 18.7 detik dan lama gempa 85-106 detik.",
            "recommendation":"Rekomendasi(1) Masyarakat di sekitar G. Ili Lewotolok maupun pengunjung/pendaki/wisatawan agar tidak memasuki dan tidak melakukan aktivitas di dalam wilayah radius 2 km dari pusat aktivitas G. Ili Lewotolok, dan masyarakat Desa Lamawolo, Desa Lamatokan, dan Desa Jontona agar selalu mewaspadai potensi ancaman bahaya dari guguran/longsoran lava dan awan panas dari bagian timur puncak/kawah G. Ili Lewotolok.(2) Untuk menghindari gangguan pernapasan (ISPA) maupun gangguan kesehatan Iainnya yang disebabkan oleh abu vulkanik maka masyarakat yang berada di sekitar G. Ili Lewotolok dapat menggunakan masker pelindung mulut dan hidung serta perlengkapan lain untuk melindungi mata dan kulit.(3) Masyarakat yang bermukim di sekitar lembah/aliran sungai-sungai yang berhulu di puncak G. Ili Lewotolok agar selalu mewaspadai potensi ancaman bahaya lahar yang dapat terjadi terutama di saat musim hujan."
         }
      },
      "Karangetang":{
         "location":"Sulawesi Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214094?signature=c97fab70ceda897ade46205159d90b974256813080b429dfe447fa786de624ad",
         "detail":{
            "title":"Karangetang, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Aditya Gurasali",
            "location":"Gunung Api Karangetang terletak di Kab\\Kota Siau Tagulandang Biaro (Sitaro), Sulawesi Utara dengan posisi geografis di Latitude 2.78°LU, Longitude 125.406°BT dan memiliki ketinggian 1784 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/KAR/KAR202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-II. Teramati asap kawah utama berwarna putih dengan intensitas sedang tinggi sekitar 75-100 meter dari puncak. Cuaca berawan hingga hujan, angin lemah hingga sedang ke arah barat laut.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah hingga sedang ke arah barat laut. Suhu udara sekitar 26-29°C.",
            "seismic_observation":"Pengamatan Kegempaan6 kali gempa Guguran dengan amplitudo 10-40 mm dan lama gempa 126-161 detik.3 kali gempa Hybrid/Fase Banyak dengan amplitudo 6-20 mm, S-P tidak teramati dan lama gempa 11-21 detik.1 kali gempa Vulkanik Dalam dengan amplitudo 75 mm, S-P 1 detik dan lama gempa 18 detik.1 kali gempa Tektonik Lokal dengan amplitudo 75 mm, S-P 1 detik dan lama gempa 34 detik.8 kali gempa Tektonik Jauh dengan amplitudo 20-75 mm, S-P 14-20 detik dan lama gempa 50-73 detik.",
            "recommendation":"Rekomendasi(1) Masyarakat dan pengunjung/wisatawan agar tidak mendekati, tidak melakukan pendakian dan tidak beraktivitas di dalam zona prakiraan bahaya yaitu radius 1.5 km dari puncak Kawah Dua (Kawah Utara) dan Kawah Utama (selatan) serta area perluasan sektoral ke arah Barat sejauh 2.5 km serta sepanjang kali Malebuhe.(2) Mewaspadai guguran lava dan awan panas guguran yang dapat terjadi sewaktu-waktu dari penumpukan material lava sebelumnya karena kondisinya belum stabil dan mudah runtuh, terutama kesektor selatan, tenggara, barat dan barat daya.(3) Masyarakat yang tinggal di sekitar bantaran sungai-sungai yang berhulu dari puncak G. Karangetang agar meningkatkan kesiapsiagaan dari potensi ancaman lahar hujan dan banjir bandang yang dapat mengalir hingga ke pantai."
         }
      },
      "Kerinci":{
         "location":"Jambi, Sumatera Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214096?signature=92179361ee199b7aa21dec3d0691fdfb1316237c7ca2ae4596502a76965e5815",
         "detail":{
            "title":"Kerinci, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Irwan Safwan",
            "location":"Gunung Api Kerinci terletak di Kab\\Kota Kerinci, Solok Selatan, Jambi, Sumatera Barat dengan posisi geografis di Latitude -1.697°LU, Longitude 101.264°BT dan memiliki ketinggian 3805 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/KER/KER202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-II. Asap kawah nihil. Cuaca cerah, angin lemah hingga sedang ke arah timur laut dan barat.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca cerah, angin lemah hingga sedang ke arah timur laut dan barat. Suhu udara sekitar 16-25°C. Kelembaban 58-70%.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Vulkanik Dalam dengan amplitudo 10 mm, S-P tidak teramati dan lama gempa 17 detik.1 kali gempa Tremor Menerus dengan amplitudo 0.5-3 mm, dominan 1 mm.",
            "recommendation":"Rekomendasi1. Masyarakat disekitar gunungapi kerinci dan pengunjung/wisatawan tidak diperbolehkan mendaki kawah yang ada dipuncak gunungapi kerinci didalam radius 3 km dari kawah aktif (masyarakat dilarang beraktifitas didalam radius bahaya/KRB III).2. Sebaiknya jalur penerbangan disekitar gunungapi kerinci dihindari karena sewaktu-waktu masih memiliki potensi letusan abu dengan ketinggian yang dapat mengganggu jalur penerbangan."
         }
      },
      "Lokon":{
         "location":"Sulawesi Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214084?signature=b32fe2d8ee986343f10bf5ce7d1f46503509098732aa2893421176d7328c6c0c",
         "detail":{
            "title":"Lokon, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Farid Ruskanda Bina",
            "location":"Gunung Api Lokon terletak di Kab\\Kota Tomohon, Sulawesi Utara dengan posisi geografis di Latitude 1.358°LU, Longitude 124.792°BT dan memiliki ketinggian 1580 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/LOK/LOK202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Teramati asap kawah utama berwarna putih dengan intensitas tipis hingga sedang tinggi sekitar 25-30 meter dari puncak. Cuaca cerah hingga hujan, angin lemah ke arah selatan.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca cerah hingga hujan, angin lemah ke arah selatan. Suhu udara sekitar 20-26°C. Intensitas curah hujan 8 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan1 kali Tremor Non-Harmonik dengan amplitudo 5 mm, dan lama gempa 120 detik.3 kali gempa Vulkanik Dangkal dengan amplitudo 3-6 mm, dan lama gempa 3-6 detik.2 kali gempa Tektonik Jauh dengan amplitudo 4-44 mm, S-P tidak teramati dan lama gempa 70-150 detik.",
            "recommendation":"Rekomendasi(1)Masyarakat dan wisatawan untuk tidak mendekati dan melakukan aktivitas di dalam radius 1.5 km dari Kawah Tompaluan (Pusat Aktivitas)(2)Jika terjadi letusan & hujan abu, masyarakat di himbau untuk tetap berada di dalam rumah, dan apabila berada di luar rumah disarankan untuk menggunakan pelindung hidung, mulut (masker) dan mata (kacamata).(3)Mewaspadai potensi lahar pada sungai-sungai yang berhulu dari puncak G. Lokon terutama pada musim hujan."
         }
      },
      "Marapi":{
         "location":"Sumatera Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214104?signature=d815a089a9def4b2e829a7d572f10b0d08a892c640225f7824640139d4b584df",
         "detail":{
            "title":"Marapi, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Asep Antoni",
            "location":"Gunung Api Marapi terletak di Kab\\Kota Agam, Batusangkar, Sumatera Barat dengan posisi geografis di Latitude -0.381°LU, Longitude 100.473°BT dan memiliki ketinggian 2891 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/MAR/MAR202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-I. Teramati asap kawah utama berwarna putih dan kelabu dengan intensitas tipis, sedang hingga tebal tinggi sekitar 75-100 meter dari puncak. Cuaca cerah hingga berawan, angin lemah ke arah utara dan selatan.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca cerah hingga berawan, angin lemah ke arah utara dan selatan. Suhu udara sekitar 18.7-28.7°C. Kelembaban 44.8-83.4%. Tekanan udara 680.6-681.4 mmHg.",
            "seismic_observation":"Pengamatan Kegempaan3 kali gempa Letusan/Erupsi dengan amplitudo 1.9-5.5 mm, dan lama gempa 79-112 detik.17 kali gempa Hembusan dengan amplitudo 1.2-2.5 mm, dan lama gempa 39-141 detik.2 kali gempa Tektonik Lokal dengan amplitudo 21.4-21.6 mm, S-P 2.5 detik dan lama gempa 25-30 detik.1 kali gempa Tremor Menerus dengan amplitudo 0.5-2.5 mm, dominan 1 mm.",
            "recommendation":"RekomendasiMasyarakat disekitar Gunungapi Marapi dan pengunjung/wisatawan tidak diperbolehkan mendaki Gunungapi Marapi pada radius 3Km dari kawah/puncak."
         }
      },
      "Raung":{
         "location":"Jawa Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214092?signature=0f838bbb86a414917bc1492f84eb723ed26cca8af56b12b7662a93afa552ce0c",
         "detail":{
            "title":"Raung, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Burhan Alethea",
            "location":"Gunung Api Raung terletak di Kab\\Kota Banyuwangi, Bondowoso, Jember, Jawa Timur dengan posisi geografis di Latitude -8.125°LU, Longitude 114.042°BT dan memiliki ketinggian 3332 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/RAU/RAU202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Teramati asap kawah utama berwarna putih dengan intensitas sedang tinggi sekitar 100-200 meter dari puncak. Cuaca berawan hingga hujan, angin lemah ke arah selatan.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah ke arah selatan. Suhu udara sekitar 20-32°C. Intensitas curah hujan 2.7 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan17 kali gempa Hembusan dengan amplitudo 2-3 mm, dan lama gempa 22-46 detik.7 kali gempa Tektonik Jauh dengan amplitudo 2-32 mm, S-P 14-83 detik dan lama gempa 62-170 detik.1 kali gempa Tremor Menerus dengan amplitudo 0.5-2 mm, dominan 0.5 mm.",
            "recommendation":"RekomendasiMasyarakat dan pengunjung/wisatawan tidak diperbolehkan mendekati pusat erupsi di kawah puncak dengan radius 3 km."
         }
      },
      "Rinjani":{
         "location":"Nusa Tenggara Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214108?signature=de6478de709bade763511e83e4a58d3339af04a0c28b361165a89659bf02da1e",
         "detail":{
            "title":"Rinjani, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Albertus Galih Prasida Kastawa",
            "location":"Gunung Api Rinjani terletak di Kab\\Kota Lombok Timur, Nusa Tenggara Barat dengan posisi geografis di Latitude -8.42°LU, Longitude 116.47°BT dan memiliki ketinggian 3726 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/RIN/RIN202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-II. Asap kawah tidak teramati. Cuaca berawan hingga hujan, angin lemah ke arah timur dan barat.",
            "other_description":"Tidak Ada",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah ke arah timur dan barat. Suhu udara sekitar 15-18°C. Kelembaban 94%. Intensitas curah hujan 12 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Low Frequency dengan amplitudo 2.4 mm, dan lama gempa 76 detik.5 kali gempa Vulkanik Dalam dengan amplitudo 2.2-4.1 mm, S-P 0.94-3.53 detik dan lama gempa 12-20 detik.3 kali gempa Tektonik Lokal dengan amplitudo 4.5-18.5 mm, S-P 4.3-6.7 detik dan lama gempa 24-26 detik.5 kali gempa Tektonik Jauh dengan amplitudo 1.7-6 mm, S-P 12.9-81.5 detik dan lama gempa 40-158 detik.",
            "recommendation":"Rekomendasi(1)Masyarakat di sekitar G. Rinjani dan pendaki/pengunjung/wisatawan agar tidak beraktivitas/berkemah di dalam area tubuh G. Barujari termasuk di area lava baru dan seluruh area di dalam radius 1,5 km dari kawah G. Barujari.(2) Pendakian diperbolehkan kecuali di seluruh bagian tubuh G. Barujari (lihat poin 1), karena material lava letusan masih bertemperatur tinggi dan tidak stabil sehingga rawan untuk terjadi rockfall/longsoran batu.(3)Meskipun tidak dapat dipastikan, namun potensi letusan G. Rinjani masih ada. Oleh karena itu pendaki/pengunjung/wisatawan yang beraktivitas di luar radius 1,5 km dari G. Barujari maupun masyarakat di sekitar G. Rinjani diharapkan untuk selalu menyiapkan masker, penutup hidung dan mulut serta pelindung mata agar terhindar dari infeksi saluran pernapasan akut (ISPA) dan iritasi mata jika terjadi letusan abu.(4)Masyarakat di sekitar G. Rinjani diharap untuk tetap tenang namun tetap menjaga  kewaspadaan, tidak terpancing isu-isu tentang erupsi G. Rinjani yang tidak jelas sumbernya."
         }
      },
      "Sangeangapi":{
         "location":"Nusa Tenggara Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214101?signature=0aceea14ae97077f8be663027acbe540f8afd44878d80dddd8c5883923ab738d",
         "detail":{
            "title":"Sangeangapi, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Ari Yuda Recky Ferlando",
            "location":"Gunung Api Sangeangapi terletak di Kab\\Kota Bima, Nusa Tenggara Barat dengan posisi geografis di Latitude -8.2°LU, Longitude 119.07°BT dan memiliki ketinggian 1949 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/SAN/SAN202302022400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-I hingga tertutup Kabut 0-III. Asap kawah nihil. Cuaca berawan hingga hujan, angin lemah hingga sedang ke arah timur dan tenggara.",
            "other_description":"Seismik off",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah hingga sedang ke arah timur dan tenggara. Suhu udara sekitar 28-31°C. Kelembaban 75-85%.",
            "seismic_observation":"Pengamatan KegempaanNihil",
            "recommendation":"Rekomendasi(1)Masyarakat di sekitar G. Sangeangapi dan pengunjung/wisatawan agar tidak beraktivitas di dalam radius 1.5 km dari kawah G. Sangeangapi.(2) Masyarakat di sekitar G. Sangeangapi dan pengunjung/wisatawan agar mewaspadai bahaya aliran piroklastik serta tidak diperbolehkan mendekati dan beraktivitas di daerah di antara Lembah Sori Wala dan Sori Mantau hingga mencapai pantai, serta pada  Lembah Sori Boro dan Sori Oi.(3) Masyarakat, petani, pengunjung/wisatawan tidak diperbolehkan mendekati dan beraktivitas pada semua lembah sungai yang berhulu dari pusat aktivitas/puncak G. Sangeangapi untuk menghindari potensi ancaman bahaya aliran lahar yang mungkin terjadi pada saat hujan."
         }
      },
      "Sinabung":{
         "location":"Sumatera Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214090?signature=4b1e474ac8ce3cd5ef4705dc7cf61c83aeeac36e664c0bb1bd1f2e1f3769b8ec",
         "detail":{
            "title":"Sinabung, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Armen Putra",
            "location":"Gunung Api Sinabung terletak di Kab\\Kota Karo, Sumatera Utara dengan posisi geografis di Latitude 3.17°LU, Longitude 98.392°BT dan memiliki ketinggian 2460 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/SIN/SIN202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-II. Teramati asap kawah utama berwarna putih dengan intensitas tipis hingga tebal tinggi sekitar 100-300 meter dari puncak. Cuaca cerah hingga hujan, angin lemah ke arah timur dan tenggara.",
            "other_description":"Terekam Noise Petir",
            "climatology":"KlimatologiCuaca cerah hingga hujan, angin lemah ke arah timur dan tenggara. Suhu udara sekitar 16-25°C. Intensitas curah hujan 1 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Hybrid/Fase Banyak dengan amplitudo 4 mm, S-P 1 detik dan lama gempa 17 detik.1 kali gempa Tektonik Lokal dengan amplitudo 2 mm, S-P 7 detik dan lama gempa 23 detik.1 kali gempa Tektonik Jauh dengan amplitudo 5 mm, S-P 19 detik dan lama gempa 42 detik.",
            "recommendation":"Rekomendasi1. Masyarakat dan pengunjung/wisatawan agar tidak melakukan aktivitas pada desa-desa yang sudah direlokasi, serta lokasi di dalam radius radial 3 km dari puncak G.Sinabung, serta radius 4.5 km untuk sektoral selatan-timur2. Masyarakat yang berada dan bermukim di dekat sungai-sungai yang berhulu di G. Sinabung agar tetap waspada terhadap bahaya lahar.3. Pemerintah Daerah Kabupaten Karo agar senantiasa berkoordinasi dengan Pusat Vulkanologi dan Mitigasi Bencana Geologi atau Pos Pengamatan Gunung api Sinabung"
         }
      },
      "Soputan":{
         "location":"Sulawesi Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214131?signature=ec21a8754ad794ebdb09c2efbe79da6744934303204b4778af2f4198bf63c6d5",
         "detail":{
            "title":"Soputan, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Fahrul Roji",
            "location":"Gunung Api Soputan terletak di Kab\\Kota Minahasa Tenggara, Sulawesi Utara dengan posisi geografis di Latitude 1.1145°LU, Longitude 124.737°BT dan memiliki ketinggian 1809 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/SOP/SOP202302022400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-II hingga tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca berawan hingga hujan, angin lemah hingga sedang ke arah tenggara.",
            "other_description":"Seismogram didominasi nois angin",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah hingga sedang ke arah tenggara. Suhu udara sekitar 19-29°C. Intensitas curah hujan 14 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan3 kali gempa Guguran dengan amplitudo 5-6 mm dan lama gempa 10-18 detik.1 kali gempa Low Frequency dengan amplitudo 3 mm, dan lama gempa 9 detik.6 kali gempa Tektonik Jauh dengan amplitudo 3-40 mm, S-P tidak teramati dan lama gempa 35-140 detik.",
            "recommendation":"Rekomendasi(1)Masyarakat di sekitar G. Soputan maupun pengunjung/wisatawan/pendaki agar tidak beraktivitas di dalam radius 1.5 km dari puncak G. Soputan dan dalam wilayah sektoral arah barat-baratlaut sejauh 2.5 km yang merupakan daerah bukaan kawah, guna menghindari ancaman leleran lava dan awan panas guguran.(2)Masyarakat yang bermukim/beraktivitas disekitar bantaran sungai yang berhulu di sekitar lereng G. Soputan juga di rekomendasikan agar mewaspadai terjadinya ancaman aliran lahar terutama ketika musim hujan, beberapa sungai yang perlu diwaspadai  di antaranya adalah S. Ranowangko, S. Lawian,  S. Popang dan Londola Kelewahu.(3)Jika terjadi hujan abu, masyarakat dianjurkan menggunakan masker penutup hidung dan mulut, guna mengantisipasi terhadap gangguan saluran pernapasan."
         }
      }
   },
   "Level I (Normal)":{
      "Agung":{
         "location":"Bali",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214117?signature=d547e1a02dee6b4de79750ed289f3e50fccfdeeb2a47ded2446c88edb3a136e7",
         "detail":{
            "title":"Agung, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Wahyu Ardi Setiawan",
            "location":"Gunung Api Agung terletak di Kab\\Kota Karangasem, Bali dengan posisi geografis di Latitude -8.342°LU, Longitude 115.508°BT dan memiliki ketinggian 3142 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/AGU/AGU202302022400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-I hingga tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca berawan hingga hujan, angin lemah ke arah timur.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah ke arah timur. Suhu udara sekitar 19-29°C. Kelembaban 64-97%.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Tektonik Jauh dengan amplitudo 23 mm, S-P 16 detik dan lama gempa 55 detik.",
            "recommendation":"Rekomendasi(1)  Masyarakat di sekitar G. Agung dan pendaki/pengunjung/wisatawan direkomendasikan agar membatasi aktivitas di area kawah puncak G. Agung.(2) Masyarakat yang bermukim dan beraktivitas di sekitar aliran-aliran sungai yang berhulu di G. Agung agar mewaspadai potensi ancaman bahaya sekunder berupa aliran lahar hujan yang dapat terjadi terutama pada musim hujan dan jika material erupsi masih terpapar di area puncak. Area potensi landaan aliran lahar hujan mengikuti aliran-aliran sungai yang berhulu di G. Agung."
         }
      },
      "Ambang":{
         "location":"Sulawesi Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214130?signature=f84739326681c17601400aa51c82abad8e4881169b8607256bccf376f814e6c4",
         "detail":{
            "title":"Ambang, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Purwadi Sucipto",
            "location":"Gunung Api Ambang terletak di Kab\\Kota Bolaang Mongondow, Sulawesi Utara dengan posisi geografis di Latitude 0.75°LU, Longitude 124.42°BT dan memiliki ketinggian 1795 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/AMB/AMB202302022400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca berawan hingga mendung, angin lemah hingga sedang ke arah timur.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga mendung, angin lemah hingga sedang ke arah timur. Suhu udara sekitar 26-31°C. Kelembaban 69-72%.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Tektonik Jauh dengan amplitudo 45 mm, S-P tidak teramati dan lama gempa 78.44 detik.",
            "recommendation":"RekomendasiMasyarakat disekitar G. Ambang dan pengunjung /wisatawan membatasi aktivitas (tidak berlama - lama dan tidak bermalam di area kawah aktif),serta tidak mendekati lubang hembusan gas yang berada di sekitar kawah untuk menghindari potensi bahaya gas beracun."
         }
      },
      "Anak Ranakah":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214107?signature=a368322efa5a613fcc0e5ace8c84741293c7a471b2ffc3d1fb59fe9d0dc133b5",
         "detail":{
            "title":"Anak Ranakah, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Andrik Kurnia Adi Pratama",
            "location":"Gunung Api Anak Ranakah terletak di Kab\\Kota Manggarai, Nusa Tenggara Timur dengan posisi geografis di Latitude -8.62°LU, Longitude 120.52°BT dan memiliki ketinggian 2350 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/RAN/RAN202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca cerah hingga hujan, angin lemah ke arah barat.",
            "other_description":"Seismograf MEQ-800 belum beroperasi",
            "climatology":"KlimatologiCuaca cerah hingga hujan, angin lemah ke arah barat. Suhu udara sekitar 17-25°C. Kelembaban 80-95%. Intensitas curah hujan 1.75 mm per hari.",
            "seismic_observation":"Pengamatan KegempaanNihil",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Anak Ranakah maupun pengunjung wisatawan/pendaki agar tidak beraktifitas didalam area kawah aktif, serta tidak mendekati lubang tembusan gas yang berada disekitar kawah untuk menghindari potensi gas beracun dan juga membatasi aktifitas (tidak berlama-lama) disekitar area kawah."
         }
      },
      "Arjuno Welirang":{
         "location":"Jawa Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214133?signature=3afd8b498d89b6ce6b783b04f26b233a10bf883a1ebcc025798e1f066b164895",
         "detail":{
            "title":"Arjuno Welirang, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Kuswarno",
            "location":"Gunung Api Arjuno Welirang terletak di Kab\\Kota Malang, Mojokerto, Pasuruan, Jawa Timur dengan posisi geografis di Latitude -7.725°LU, Longitude 112.58°BT dan memiliki ketinggian 3339 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/WEL/WEL202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Teramati asap kawah utama berwarna putih dengan intensitas tipis hingga sedang tinggi sekitar 20-30 meter dari puncak. Cuaca cerah hingga hujan, angin lemah hingga sedang ke arah timur.",
            "other_description":"Seismik didominasi nois angin",
            "climatology":"KlimatologiCuaca cerah hingga hujan, angin lemah hingga sedang ke arah timur. Suhu udara sekitar 25-30°C.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Hembusan dengan amplitudo 1 mm, dan lama gempa 27.43 detik.1 kali gempa Tektonik Jauh dengan amplitudo 3 mm, S-P 23.36 detik dan lama gempa 86.37 detik.",
            "recommendation":"RekomendasiPenduduk/ masyarakat di sekitar G. ArjunoWelirang dan pengunjung / wisatawan/ pendaki dilarang memasuki areal kawah aktif G. ArjunoWelirang ."
         }
      },
      "Batur":{
         "location":"Bali",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214126?signature=c6780eebf63233253bbbc23424777effcf8a0ae7252e1b65cfae5cffacea42c2",
         "detail":{
            "title":"Batur, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Achmad Nurin Kausar",
            "location":"Gunung Api Batur terletak di Kab\\Kota Bangli, Bali dengan posisi geografis di Latitude -8.242°LU, Longitude 115.375°BT dan memiliki ketinggian 1717 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/BAT/BAT202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Asap kawah nihil. Cuaca berawan hingga hujan, angin lemah ke arah utara.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah ke arah utara. Suhu udara sekitar 16-22°C. Kelembaban 90-92%. Intensitas curah hujan 5.4 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Tektonik Jauh dengan amplitudo 2 mm, S-P tidak teramati dan lama gempa 52 detik.",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Batur dan pengunjung/wisatawan agar membatasi aktivitas (tidak berlama-lama) dan tidak bermalam di area kawah aktif, serta tidak mendekati lubang tembusan gas yang berada di sekitar kawah untuk menghindari potensi bahaya gas beracun."
         }
      },
      "Batutara":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214036?signature=93c193a2bc2f1dcd1fceb0d9ce52f64812bf372aa45aecdec1a21228be5a64a3",
         "detail":{
            "title":"Batutara, Rabu - 01 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Fajaruddin M. Balido",
            "location":"Gunung Api Batutara terletak di Kab\\Kota Lembata, Nusa Tenggara Timur dengan posisi geografis di Latitude -7.792°LU, Longitude 123.579°BT dan memiliki ketinggian 748 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/TAR/TAR202302012400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca cerah hingga hujan, angin lemah hingga sedang ke arah timur dan tenggara.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca cerah hingga hujan, angin lemah hingga sedang ke arah timur dan tenggara. Suhu udara sekitar 24.8-30.2°C. Kelembaban 67.3-88.5%.",
            "seismic_observation":"Pengamatan KegempaanNihil",
            "recommendation":"RekomendasiMasyarakat dan pengunjung/wisatawan agar tidak mengunjungi/memasuki Pulau Batutara."
         }
      },
      "Bur Ni Telong":{
         "location":"Aceh",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214113?signature=d721ac8315da393ba97a5414167c94415bc71426d0a09d6eee5236513e16f750",
         "detail":{
            "title":"Bur Ni Telong, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Ihsan Nopa Abadi",
            "location":"Gunung Api Bur Ni Telong terletak di Kab\\Kota Aceh Tengah, Aceh dengan posisi geografis di Latitude 4.769°LU, Longitude 96.821°BT dan memiliki ketinggian 2623 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/TEL/TEL202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Asap kawah nihil. Cuaca cerah hingga mendung, angin lemah hingga sedang ke arah timur.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca cerah hingga mendung, angin lemah hingga sedang ke arah timur. Suhu udara sekitar 18-28°C. Kelembaban 90-91%.",
            "seismic_observation":"Pengamatan Kegempaan2 kali gempa Tektonik Lokal dengan amplitudo 12-37 mm, S-P 6-7 detik dan lama gempa 39-56 detik.",
            "recommendation":"RekomendasiMasyarakat dan pengunjung/pendaki Gunung Api Bur Ni Telong tidak diperbolehkan berada di daerah fumarola dan solfatara pada saat cuaca mendung atau hujan karena konsentrasi gas dapat membahayakan kehidupan."
         }
      },
      "Ciremai":{
         "location":"Jawa Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214105?signature=93b8e797486d59b46490706b2b0e3c42800a675532006e2be8d2f2f2953b170f",
         "detail":{
            "title":"Ciremai, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Andri Yunianto",
            "location":"Gunung Api Ciremai terletak di Kab\\Kota Cirebon, Kuningan, Majalengka, Jawa Barat dengan posisi geografis di Latitude -6.892°LU, Longitude 108.4°BT dan memiliki ketinggian 3078 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/CER/CER202302022400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-II hingga tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca cerah hingga hujan, angin lemah hingga sedang ke arah barat.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca cerah hingga hujan, angin lemah hingga sedang ke arah barat. Suhu udara sekitar 20-27°C.",
            "seismic_observation":"Pengamatan Kegempaan3 kali gempa Tektonik Jauh dengan amplitudo 3-12.5 mm, S-P 12.2-32.4 detik dan lama gempa 46.7-141.8 detik.",
            "recommendation":"RekomendasiMasyarakat dan pengunjung/wisatawan tidak diperbolehkan turun ke dasar kawah dan dalam kondisi mendung/hujan agar tidak mendekat ke kawah."
         }
      },
      "Colo":{
         "location":"Sulawesi Tengah",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214098?signature=dd48190e7d7e53c4a1817d45da7c74209f0d0578cb29afac03979bf97f3e95a0",
         "detail":{
            "title":"Colo, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Abdul Farid N. Baginda",
            "location":"Gunung Api Colo terletak di Kab\\Kota Tojo Una-una, Sulawesi Tengah dengan posisi geografis di Latitude -0.162°LU, Longitude 121.601°BT dan memiliki ketinggian 404 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/COL/COL202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca cerah hingga hujan, angin sedang hingga kencang ke arah timur.",
            "other_description":"Seismograf dlm perbaikan",
            "climatology":"KlimatologiCuaca cerah hingga hujan, angin sedang hingga kencang ke arah timur. Suhu udara sekitar 27.5-31.5°C. Kelembaban 55-67%.",
            "seismic_observation":"Pengamatan KegempaanNihil",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Colo dan pengunjung/wisatawan agar membatasi aktivitas (tidak berlama-lama) dan tidak bermalam di area kawah aktif, serta tidak mendekati lubang tembusan gas yang berada di sekitar kawah untuk menghindari potensi bahaya gas beracun."
         }
      },
      "Ebulobo":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214083?signature=d219916c0e3bdfb40402c0f3fcaf9e6f26ad89014f31924a82d7f786fc5c1c95",
         "detail":{
            "title":"Ebulobo, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Yuvensius Nggaa",
            "location":"Gunung Api Ebulobo terletak di Kab\\Kota Nagekeo, Nusa Tenggara Timur dengan posisi geografis di Latitude -8.82°LU, Longitude 121.18°BT dan memiliki ketinggian 2124 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/EBU/EBU202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Teramati asap kawah utama berwarna putih dengan intensitas tipis tinggi sekitar 10-25 meter dari puncak. Cuaca cerah hingga hujan, angin lemah ke arah selatan.",
            "other_description":"2 kali hujan gerimis - deras",
            "climatology":"KlimatologiCuaca cerah hingga hujan, angin lemah ke arah selatan. Suhu udara sekitar 19-25°C. Intensitas curah hujan 34 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Tektonik Lokal dengan amplitudo 10.2 mm, S-P 5.2 detik dan lama gempa 42.1 detik.2 kali gempa Tektonik Jauh dengan amplitudo 7.4-11.1 mm, S-P 17.7-25.8 detik dan lama gempa 67.2-136.7 detik.",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Ebulobo dan pengunjung/wisatawan agar membatasi aktivitas (tidak berlama-lama) dan tidak bermalam di area kawah aktif di Utara puncak, serta tidak mendekati lubang tembusan gas yang berada di sekitar kawah untuk menghindari potensi bahaya gas beracun."
         }
      },
      "Egon":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214088?signature=b31e62e8112ec9aa039064169f8cb1f3e3f7f6520b63b87657704c59b63f3b22",
         "detail":{
            "title":"Egon, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Yosef Suryanto",
            "location":"Gunung Api Egon terletak di Kab\\Kota Sikka, Nusa Tenggara Timur dengan posisi geografis di Latitude -8.676°LU, Longitude 122.455°BT dan memiliki ketinggian 1661 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/EGO/EGO202302022400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-II hingga tertutup Kabut 0-III. Asap kawah nihil. Cuaca mendung hingga hujan, angin lemah ke arah tenggara.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca mendung hingga hujan, angin lemah ke arah tenggara. Suhu udara sekitar 25.4-33.9°C. Intensitas curah hujan 3.5 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan2 kali gempa Hembusan dengan amplitudo 4-6.5 mm, dan lama gempa 8-14 detik.1 kali gempa Vulkanik Dalam dengan amplitudo 23 mm, S-P 1 detik dan lama gempa 13 detik.3 kali gempa Tektonik Jauh dengan amplitudo 5-28 mm, S-P 13-19 detik dan lama gempa 45-105 detik.",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Egon dan pengunjung/wisatawan dapat beraktivitas seperti biasanya namun disarankan agar membatasi aktivitas (tidak berlama-lama) dan tidak bermalam di area kawah aktif, serta tidak mendekati lubang tembusan gas yang berada di sekitar area kawah untuk menghindari potensi bahaya yang mungkin terjadi, seperti di antaranya gas beracun."
         }
      },
      "Galunggung":{
         "location":"Jawa Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214097?signature=01e1913eb678a5c4c4cb7e76555bfc09b7a0c918618e2bbe6fb5fd213e064d78",
         "detail":{
            "title":"Galunggung, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" R. Fajar Anugrah",
            "location":"Gunung Api Galunggung terletak di Kab\\Kota Tasikmalaya, Garut, Jawa Barat dengan posisi geografis di Latitude -7.25°LU, Longitude 108.058°BT dan memiliki ketinggian 2168 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/GAL/GAL202302022400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-I hingga tertutup Kabut 0-II. Asap kawah tidak teramati. Cuaca berawan hingga hujan, angin lemah ke arah timur dan barat.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah ke arah timur dan barat. Suhu udara sekitar 21.99-30.72°C. Kelembaban 63-83%. Intensitas curah hujan 1.8 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan3 kali gempa Tektonik Jauh dengan amplitudo 4.28-66 mm, S-P 16.33-54.57 detik dan lama gempa 69.48-115.2 detik.",
            "recommendation":"Rekomendasi1. Masyarakat/pengunjung/wisatawan/pendaki tidak diperbolehkan untuk bermalam dan tidak turun ke dalam danau kawah2. Masyarakat/pengunjung tidak diperbolehkan berenang dan mengkonsumsi air danau kawah dikarenakan dapat menimbulkan keluhan atau gangguan kesehatan"
         }
      },
      "Gamkonora":{
         "location":"Maluku Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214136?signature=a94030d62729362938b70264c4e3fe8c8534c5438e3e3288e65a1d66523738cb",
         "detail":{
            "title":"Gamkonora, Kamis - 02 Februari 2023, periode 00:00-24:00 WIT",
            "author":" Taufan Barham",
            "location":"Gunung Api Gamkonora terletak di Kab\\Kota Halmahera Barat, Maluku Utara dengan posisi geografis di Latitude 1.38°LU, Longitude 127.53°BT dan memiliki ketinggian 1635 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/GMK/GMK202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Teramati asap kawah utama berwarna putih dengan intensitas tipis tinggi sekitar 30-40 meter dari puncak. Cuaca cerah hingga hujan, angin lemah hingga sedang ke arah selatan, barat daya dan barat.",
            "other_description":"Hujan gerimis",
            "climatology":"KlimatologiCuaca cerah hingga hujan, angin lemah hingga sedang ke arah selatan, barat daya dan barat. Suhu udara sekitar 27-31°C.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Tornillo dengan amplitudo 2 mm, dan lama gempa 11 detik.2 kali gempa Low Frequency dengan amplitudo 2-3 mm, dan lama gempa 30-35 detik.20 kali gempa Tektonik Jauh dengan amplitudo 2-17 mm, S-P 13-18 detik dan lama gempa 35-115 detik.",
            "recommendation":"Rekomendasi1. Masyarakat di sekitar G. Gamkonora dan pengunjung/wisatawan untuk tidak mendekati dan mengunjungi Kawah dalam radius 1 km dari Puncak G. Gamkonora.2. Agar masyarakat tetap mewaspadai terjadinya letusan freatik yang tidak didahului oleh gejala peningkatan vulkanik yang signifikan."
         }
      },
      "Gede":{
         "location":"Jawa Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214119?signature=bd58bd4b54086bde0688b9efdfd09c9698f091c657d68f17e3288d7ef14471b7",
         "detail":{
            "title":"Gede, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Ujang Jajat Solehudin",
            "location":"Gunung Api Gede terletak di Kab\\Kota Cianjur, Bogor, Sukabumi, Jawa Barat dengan posisi geografis di Latitude -6.77°LU, Longitude 106.965°BT dan memiliki ketinggian 2958 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/GED/GED202302022400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-I hingga tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca cerah hingga hujan, angin lemah hingga sedang ke arah tenggara dan barat daya.",
            "other_description":"Seismik didominasi nois angin ke tenggara",
            "climatology":"KlimatologiCuaca cerah hingga hujan, angin lemah hingga sedang ke arah tenggara dan barat daya. Suhu udara sekitar 19°C. Intensitas curah hujan 2.8 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan2 kali gempa Tektonik Lokal dengan amplitudo 6 mm, S-P 2 detik dan lama gempa 11-12 detik.3 kali gempa Tektonik Jauh dengan amplitudo 20-50 mm, S-P 12-28 detik dan lama gempa 90-174 detik.",
            "recommendation":"RekomendasiMasyarakat, pengunjung dan wisatawan tidak diperbolehkan turun ke dasar kawah dan dalam kondisi mendung atau hujan agar tidak mendekat ke kawah."
         }
      },
      "Guntur":{
         "location":"Jawa Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214095?signature=bd285f285adfc10d2fa8b8de1c8c0b598dcf0185f9ac4b60e7bbeebc4b325206",
         "detail":{
            "title":"Guntur, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Yuliana Jaya",
            "location":"Gunung Api Guntur terletak di Kab\\Kota Garut, Jawa Barat dengan posisi geografis di Latitude -7.143°LU, Longitude 107.84°BT dan memiliki ketinggian 2249 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/GUN/GUN202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca cerah hingga mendung, angin lemah hingga sedang ke arah timur dan selatan.",
            "other_description":"Stasiun MSG,LGP dan SDG (tiitmeter,GPS dan seismik 3 komponen) carrier off",
            "climatology":"KlimatologiCuaca cerah hingga mendung, angin lemah hingga sedang ke arah timur dan selatan. Suhu udara sekitar 21.5-31.5°C.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Vulkanik Dalam dengan amplitudo 2 mm, S-P 0.71 detik dan lama gempa 16.02 detik.4 kali gempa Tektonik Lokal dengan amplitudo 2-4 mm, S-P 1.02-1.44 detik dan lama gempa 26.41-27.56 detik.2 kali gempa Tektonik Jauh dengan amplitudo 4-20 mm, S-P 18.5 detik dan lama gempa 82.43-128.57 detik.",
            "recommendation":"RekomendasiMasyarakat dan pengunjung/ wisatawan/ pendaki dihimbau untuk tidak mendekati kawah aktif Gunungapi Guntur"
         }
      },
      "Ile Werung":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214115?signature=7f22d82f0e5f978ceefbefbe53ab9f4daf3cf1f964392bc337e71b846d2c98e2",
         "detail":{
            "title":"Ile Werung, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Wilson Wuri Wuthun",
            "location":"Gunung Api Ile Werung terletak di Kab\\Kota Lembata, Nusa Tenggara Timur dengan posisi geografis di Latitude -8.53°LU, Longitude 123.57°BT dan memiliki ketinggian 1018 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/WER/WER202302022400.png",
            "visual_observation":"Gunung api terlihat jelas. Asap kawah nihil. Cuaca mendung hingga hujan, angin lemah hingga sedang ke arah timur laut, timur dan tenggara.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca mendung hingga hujan, angin lemah hingga sedang ke arah timur laut, timur dan tenggara. Suhu udara sekitar 20-29°C.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Tektonik Lokal dengan amplitudo 10 mm, S-P 5 detik dan lama gempa 16 detik.1 kali gempa Terasa, skala I MMI dengan amplitudo 30 mm, S-P tidak teramati dan lama gempa 195 detik.2 kali gempa Tektonik Jauh dengan amplitudo 17-23 mm, S-P 11-18 detik dan lama gempa 39-75 detik.",
            "recommendation":"RekomendasiMasyarakat direkomendasikan untuk sementara waktu agar menghindar aktifitas di sekitar pantai di area lokasi bualan dan menghindar berlayar/melaut di sekitar area tersebut untuk mengantisipasi potensi perubahan /kenaikan muka air lautPVMBG terus melakukan pemantauan dan evaluasi aktifits kompleks Giunungapi ili Werung dan melakukan koorsinasi dengan BPBD setempat untuk melakukan sosialisasi."
         }
      },
      "Ili Boleng":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214079?signature=6a17eaeaef06573a9a7d7a8b6027d27b58963719c10464bb6e808b3169fccd0f",
         "detail":{
            "title":"Ili Boleng, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Nandra Widyawanto",
            "location":"Gunung Api Ili Boleng terletak di Kab\\Kota Flores Timur, Nusa Tenggara Timur dengan posisi geografis di Latitude -8.342°LU, Longitude 123.258°BT dan memiliki ketinggian 1659 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/BOL/BOL202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-II. Asap kawah nihil. Cuaca cerah hingga mendung, angin lemah ke arah barat laut.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca cerah hingga mendung, angin lemah ke arah barat laut. Suhu udara sekitar 25-30°C.",
            "seismic_observation":"Pengamatan Kegempaan10 kali gempa Hembusan dengan amplitudo 4.5-11.5 mm, dan lama gempa 32.7-51.8 detik.1 kali gempa Tektonik Lokal dengan amplitudo 3.6 mm, S-P 6.3 detik dan lama gempa 32.2 detik.4 kali gempa Tektonik Jauh dengan amplitudo 5.4-32 mm, S-P 20.3 detik dan lama gempa 49-127.1 detik.1 kali gempa Tremor Menerus dengan amplitudo 0.5 mm, dominan 0.5 mm.",
            "recommendation":"RekomendasiBerdasarkan pengamatan visual dan instrumental, status aktivitas G. Ili Boleng hingga tanggal 31 Desember 2022 berada pada Level I (NORMAL) dengan Rekomendasi :[1] Masyarakat di sekitar G. Ili Boleng dan pengunjung/wisatawan agar tidak beraktivitas dalam radius 3 km dari kawah utama di puncak G. Ili Boleng.[2] Masyarakat yang berada dalam Kawasan Rawan Bencana III harus meningkatkan kewaspadaan dengan memperhatikan arahan dari Pemerintah.[3] Untuk informasi lebih lanjut dapat menghubungi Pusat Vulkanologi dan Mitigasi Bencana Geologi, Badan Geologi (022) 7272606 di Bandung, Provinsi Jawa Barat, atau Pos Pengamatan G. Ile Boleng di Waiwerang, Kecamatan Adonara Timur"
         }
      },
      "Inielika":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/213864?signature=1db40c333c4e9bd37f1fab0547ffdab671ccdb9eadd65b3ee37fb1304b49da6f",
         "detail":{
            "title":"Inielika, Senin - 30 Januari 2023, periode 00:00-24:00 WITA",
            "author":" Yohanes Paulus Wisang",
            "location":"Gunung Api Inielika terletak di Kab\\Kota Ngada, Nusa Tenggara Timur dengan posisi geografis di Latitude -8.73°LU, Longitude 120.98°BT dan memiliki ketinggian 1559 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/LIK/LIK202301302400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-II. Asap kawah nihil. Cuaca cerah hingga hujan, angin lemah ke arah selatan.",
            "other_description":"Carrier off..diskriminator rusak",
            "climatology":"KlimatologiCuaca cerah hingga hujan, angin lemah ke arah selatan. Suhu udara sekitar 21-28°C.",
            "seismic_observation":"Pengamatan KegempaanNihil",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Inielika dan pengunjung/wisatawan agar tidak beraktivitas di dalam area kawah aktif, tidak mendekati lubang tembusan gas yang berada di sekitar kawah, serta membatasi aktivitas (tidak berlama-lama berada) di sekitar area kawah aktif"
         }
      },
      "Inierie":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214141?signature=ad6159a457ee1e92c10e65cadee3d4003d88a7d313883dcc97d1464d514b192c",
         "detail":{
            "title":"Inierie, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Marsianus Meo Lako",
            "location":"Gunung Api Inierie terletak di Kab\\Kota Ngada, Nusa Tenggara Timur dengan posisi geografis di Latitude -8.875°LU, Longitude 120.95°BT dan memiliki ketinggian 2245 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/RIE/RIE202302022400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-I hingga tertutup Kabut 0-III. Asap kawah nihil. Cuaca berawan hingga hujan, angin lemah ke arah barat.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah ke arah barat. Suhu udara sekitar 18-24°C. Intensitas curah hujan 200 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan3 kali gempa Tektonik Jauh dengan amplitudo 5-35 mm, S-P 12-24 detik dan lama gempa 56-147 detik.",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Inierie dan pengunjung/wisatawan agar membatasi aktivitas (tidak berlama-lama) dan tidak bermalam di area kawah aktif, serta tidak mendekati lubang tembusan gas yang berada di sekitar kawah untuk menghindari potensi bahaya gas beracun."
         }
      },
      "Iya":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214140?signature=d7439e06a97c91c3404aaf259ea28845619b02082ce0507fefdacb7c2548ad03",
         "detail":{
            "title":"Iya, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Robertus Belarminus Dua",
            "location":"Gunung Api Iya terletak di Kab\\Kota Ende, Nusa Tenggara Timur dengan posisi geografis di Latitude -8.897°LU, Longitude 121.645°BT dan memiliki ketinggian 637 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/IYA/IYA202302022400.png",
            "visual_observation":"Gunung api terlihat jelas. Asap kawah nihil. Cuaca berawan hingga mendung, angin lemah ke arah barat laut.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga mendung, angin lemah ke arah barat laut. Suhu udara sekitar 20-34°C. Kelembaban 80-82%. Tekanan udara 753-754 mmHg.",
            "seismic_observation":"Pengamatan Kegempaan2 kali gempa Vulkanik Dalam dengan amplitudo 29.5-39 mm, S-P 3.35-3.78 detik dan lama gempa 33.16-40.93 detik.1 kali gempa Tektonik Lokal dengan amplitudo 37 mm, S-P 5.2 detik dan lama gempa 43.05 detik.2 kali gempa Tektonik Jauh dengan amplitudo 7-9.5 mm, S-P 13.28-36.02 detik dan lama gempa 57.99-118.22 detik.",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Iya dan pengunjung/wisatawan agar membatasi aktivitas (tidak berlama-lama) dan tidak bermalam di area kawah aktif, serta tidak mendekati lubang tembusan gas yang berada di sekitar kawah untuk menghindari potensi bahaya gas beracun."
         }
      },
      "Kaba":{
         "location":"Bengkulu",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214099?signature=7724037ed7a1a99cfb9c3064c08671a7856cb360a765c54c58dbac075e5b1b5b",
         "detail":{
            "title":"Kaba, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Bagus Puguh Wibowo",
            "location":"Gunung Api Kaba terletak di Kab\\Kota Rejang Lebong, Bengkulu dengan posisi geografis di Latitude -3.52°LU, Longitude 102.62°BT dan memiliki ketinggian 1952 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/KAB/KAB202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-II. Asap kawah tidak teramati. Cuaca berawan, angin lemah hingga sedang ke arah timur dan barat.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan, angin lemah hingga sedang ke arah timur dan barat. Suhu udara sekitar 19-25°C.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Tektonik Jauh dengan amplitudo 5 mm, S-P 18 detik dan lama gempa 145 detik.",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Kaba maupun pengunjung/wisatawan agar membatasi aktivitas di sekitar kawah, tidak mendekati danau kawah, tidak bermalam di dalam area kawah aktif, dan tidak mendekati lubang tembusan gas untuk menghindari potensi bahaya gas beracun."
         }
      },
      "Kelimutu":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214134?signature=6314352ff60b6d93bc78569496a975ca5fe96dabfcdd45656e51144234809e68",
         "detail":{
            "title":"Kelimutu, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Gabriel Rago",
            "location":"Gunung Api Kelimutu terletak di Kab\\Kota Ende, Nusa Tenggara Timur dengan posisi geografis di Latitude -8.77°LU, Longitude 121.82°BT dan memiliki ketinggian 1639 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/KLM/KLM202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-II. Asap kawah tidak teramati. Cuaca cerah hingga hujan, angin lemah ke arah barat laut.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca cerah hingga hujan, angin lemah ke arah barat laut. Suhu udara sekitar 22.4-25.1°C. Tekanan udara 913.4-916.5 mmHg. Intensitas curah hujan 1.3 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan5 kali gempa Vulkanik Dalam dengan amplitudo 6-17 mm, S-P 1.23-3.61 detik dan lama gempa 22.8-26.62 detik.2 kali gempa Tektonik Jauh dengan amplitudo 45 mm, S-P 13.33-40.83 detik dan lama gempa 78.65-234.77 detik.",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Kelimutu dan pengunjung/wisatawan agar membatasi aktivitas di sekitar area kawah dengan tidak melewati pagar pembatas, tidak mendekati kawah danau, dan tidak bermalam di dalam kawah untuk menghindari potensi bahaya gas beracun."
         }
      },
      "Kelud":{
         "location":"Jawa Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214120?signature=45c568efe9c3da45791653a38c7a3ea97fe698c88048c331c3d9e88f33c75d66",
         "detail":{
            "title":"Kelud, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Dany Erlangga Yosa Putra",
            "location":"Gunung Api Kelud terletak di Kab\\Kota Kediri, Blitar, Malang, Jawa Timur dengan posisi geografis di Latitude -7.93°LU, Longitude 112.308°BT dan memiliki ketinggian 1731 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/KLD/KLD202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-II. Asap kawah nihil. Cuaca berawan hingga mendung, angin lemah hingga sedang ke arah utara, timur laut, timur dan tenggara.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga mendung, angin lemah hingga sedang ke arah utara, timur laut, timur dan tenggara. Suhu udara sekitar 21-28°C. Kelembaban 71-90%.",
            "seismic_observation":"Pengamatan Kegempaan6 kali gempa Tektonik Jauh dengan amplitudo 1-16 mm, S-P 14.83-79.84 detik dan lama gempa 73-176 detik.",
            "recommendation":"RekomendasiMasyarakat dan wisatawan untuk tidak memasuki/mendekat kawasan kawah aktif Gunungapi Kelud karena bisa terjadi aktivitas vulkanik tiba-tiba yang dapat mengancam keselamatan."
         }
      },
      "Kie Besi":{
         "location":"Maluku Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214146?signature=1cbf07e7339196401383da7adcec57e9e57f5792a5380a0b054f3061504015bc",
         "detail":{
            "title":"Kie Besi, Kamis - 02 Februari 2023, periode 00:00-24:00 WIT",
            "author":" Budi Santoso",
            "location":"Gunung Api Kie Besi terletak di Kab\\Kota Halmahera Selatan, Maluku Utara dengan posisi geografis di Latitude 0.32°LU, Longitude 127.4°BT dan memiliki ketinggian 1357 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/KIE/KIE202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Asap kawah nihil. Cuaca cerah hingga hujan, angin lemah hingga kencang ke arah selatan, barat daya dan barat.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca cerah hingga hujan, angin lemah hingga kencang ke arah selatan, barat daya dan barat. Suhu udara sekitar 25-26°C. Intensitas curah hujan 35 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Vulkanik Dalam dengan amplitudo 36 mm, S-P 3 detik dan lama gempa 20 detik.2 kali gempa Tektonik Jauh dengan amplitudo 12-31 mm, S-P tidak teramati dan lama gempa 25-250 detik.",
            "recommendation":"RekomendasiMasyarakat di sekitar Gn Kie Besi dan pengunjung/pendaki agar tidak beraktifitas dalam area kawah aktif. Tidak mendekati lubang tembusan gas, serta membatasi aktifitas/tidak berlama-lama berada disekitar kawah Gn Kie Besi Makian"
         }
      },
      "Lamongan":{
         "location":"Jawa Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214111?signature=c9e5086ea9a6facbcf8649680b9763c8d1668fa1c2b57cf0463882926fae9ddf",
         "detail":{
            "title":"Lamongan, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Susanto",
            "location":"Gunung Api Lamongan terletak di Kab\\Kota Lumajang, Jawa Timur dengan posisi geografis di Latitude -7.979°LU, Longitude 113.342°BT dan memiliki ketinggian 1651 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/LAM/LAM202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca cerah hingga mendung, angin lemah hingga kencang ke arah selatan.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca cerah hingga mendung, angin lemah hingga kencang ke arah selatan. Suhu udara sekitar 20-29°C.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Tektonik Jauh dengan amplitudo 12 mm, S-P 21 detik dan lama gempa 58 detik.",
            "recommendation":"Rekomendasi1.  Dalam Tingkat Aktivitas Level I (Normal), maka direkomendasikan agar masyarakat dan pengunjung/wisatawan/pendaki tidak turun dan mendekati dasar kawah di puncak G. Lamongan, serta tidak menginap di dalam kawasan puncak G. Lamongan.2.  BPBD Kab. Lumajang, Pemerintah Provinsi Jawa Timur agar selalu berkoordinasi dengan Pusat Vulkanologi dan Mitigasi Bencana Geologi atau melalui Pos Pengamatan Gunungapi Lamongan di Desa Tegal Randu, Kecamatan Klakah, Lumajang, tentang aktifitas Gunungapi Lamongan."
         }
      },
      "Lereboleng":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214114?signature=5d91925617e6ae2e57724e41089472cc13f1b043fb092c33c3a5fbe859ba436e",
         "detail":{
            "title":"Lereboleng, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" David Lawe Koten",
            "location":"Gunung Api Lereboleng terletak di Kab\\Kota Flores Timur, Nusa Tenggara Timur dengan posisi geografis di Latitude -8.365°LU, Longitude 122.833°BT dan memiliki ketinggian 1095 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/LER/LER202302022400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-I hingga tertutup Kabut 0-II. Asap kawah nihil. Cuaca mendung hingga hujan, angin lemah hingga sedang ke arah timur.",
            "other_description":"Hujan sedang",
            "climatology":"KlimatologiCuaca mendung hingga hujan, angin lemah hingga sedang ke arah timur.",
            "seismic_observation":"Pengamatan KegempaanNihil",
            "recommendation":"RekomendasiMasyarakat disekitar gunungapi Lereboleng dan pengunjung / wisatawan agar jangan beraktifitas atau berlama - lama di dalam kawah dan jangan mendekati lubang tembusan gas untuk menghindari bahaya gas beracun"
         }
      },
      "Lewotobi Laki-laki":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214121?signature=33e22f1596528aee9152a6461a49ff6825fefb6477ec0c2ba3be67c3c7294adf",
         "detail":{
            "title":"Lewotobi Laki-laki, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Herman Yosef S Mboro",
            "location":"Gunung Api Lewotobi Laki-laki terletak di Kab\\Kota Flores Timur, Nusa Tenggara Timur dengan posisi geografis di Latitude -8.5389°LU, Longitude 122.7682°BT dan memiliki ketinggian 1584 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/LWK/LWK202302022400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-I hingga tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca mendung hingga hujan, angin lemah ke arah timur.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca mendung hingga hujan, angin lemah ke arah timur. Suhu udara sekitar 22-27°C.",
            "seismic_observation":"Pengamatan Kegempaan2 kali gempa Tektonik Jauh dengan amplitudo 29.6-37 mm, S-P 14-28 detik dan lama gempa 67-164 detik.",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Lewotobi Laki-laki dan pengunjung/wisatawan agar membatasi aktivitas (tidak berlama-lama) dan tidak bermalam di area kawah aktif, serta tidak mendekati lubang tembusan gas yang berada di sekitar kawah untuk menghindari potensi bahaya gas beracun."
         }
      },
      "Lewotobi Perempuan":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214129?signature=d315cbb112543887ade8230eba0e892aed8f91fe1db8072acc34581a62f4f3c9",
         "detail":{
            "title":"Lewotobi Perempuan, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Bernadinus Dinu Tobi",
            "location":"Gunung Api Lewotobi Perempuan terletak di Kab\\Kota Flores Timur, Nusa Tenggara Timur dengan posisi geografis di Latitude -8.5539°LU, Longitude 122.7805°BT dan memiliki ketinggian 1703 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/LWP/LWP202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca berawan hingga hujan, angin lemah ke arah timur.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah ke arah timur. Suhu udara sekitar 26-28°C.",
            "seismic_observation":"Pengamatan Kegempaan2 kali gempa Tektonik Jauh dengan amplitudo 29.6-37 mm, S-P 14-28 detik dan lama gempa 67-164 detik.",
            "recommendation":"RekomendasiMasyarakat disekitar G. Lewotobi Perempuan dan pengunjung, agar membatasi aktifitas( tidak berlama lama) dan tidak bermalam di area kawah aktif,serta tidak mendekati lubang tembusan gas yang berada disekitar kawah untuk menghindari potensi bahaya gas beracun."
         }
      },
      "Mahawu":{
         "location":"Sulawesi Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214086?signature=9bba5e6e5280cfdca75dc2d899327a695094a909385d254bf1184fb58b73365e",
         "detail":{
            "title":"Mahawu, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Farid Ruskanda Bina",
            "location":"Gunung Api Mahawu terletak di Kab\\Kota Tomohon, Sulawesi Utara dengan posisi geografis di Latitude 1.352°LU, Longitude 124.865°BT dan memiliki ketinggian 1299 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/MAH/MAH202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Asap kawah nihil. Cuaca cerah hingga hujan, angin lemah ke arah selatan.",
            "other_description":"Pesawat carrier off",
            "climatology":"KlimatologiCuaca cerah hingga hujan, angin lemah ke arah selatan. Suhu udara sekitar 20-26°C. Intensitas curah hujan 8 mm per hari.",
            "seismic_observation":"Pengamatan KegempaanNihil",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Mahawu dan pengunjung/wisatawan agar membatasi aktivitas (tidak berlama-lama) dan tidak bermalam di area kawah aktif, serta tidak mendekati lubang hembusan gas yang berada di sekitar kawah untuk menghindari potensi bahaya gas beracun."
         }
      },
      "Papandayan":{
         "location":"Jawa Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214122?signature=65ea0f3ef39e9eaaf60d532eea22529cdfbf80414d9167db7d82350638d39307",
         "detail":{
            "title":"Papandayan, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Johan Kusuma",
            "location":"Gunung Api Papandayan terletak di Kab\\Kota Garut, Jawa Barat dengan posisi geografis di Latitude -7.32°LU, Longitude 107.73°BT dan memiliki ketinggian 2665 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/PAP/PAP202302022400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-II hingga tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca berawan hingga hujan, angin lemah hingga sedang ke arah timur laut dan selatan.",
            "other_description":"Rekaman gempa dominasi noise angin pada dini hari",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah hingga sedang ke arah timur laut dan selatan. Suhu udara sekitar 19-23°C.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Tektonik Lokal dengan amplitudo 5 mm, S-P 3 detik dan lama gempa 12 detik.4 kali gempa Tektonik Jauh dengan amplitudo 4-31 mm, S-P 16-23 detik dan lama gempa 51-105 detik.",
            "recommendation":"RekomendasiA.\tMasyarakat di sekitar G. Papandayan dan pengunjung, wisatawan, pendaki tidak diperbolehkan beraktivitas dan menginap dalam kawasan bukaan kawah aktif yang ada di dalam kompleks G. Papandayan yaitu : Kawah Baru, Kawah Emas, Kawah Nangklak, Kawah Manuk/Balagadama dalam radius 500 meter, serta ketika cuaca mendung dan hujan.B.\tMasyarakat di sekitar G. Papandayan, pedagang, wisatawan, pendaki, dan pengelola wisata G. Papandayan agar mewaspadai terjadinya letusan freatik yang bersifat tiba-tiba dan  tanpa didahului oleh gejala-gejala vulkanik yang jelas."
         }
      },
      "Peut Sague":{
         "location":"Daerah Istimewa Aceh",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214124?signature=e1da786750d7466230fa9f182d0d84ff933a06669250d620af0441fbcf19c0fa",
         "detail":{
            "title":"Peut Sague, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Muhammad Nazir",
            "location":"Gunung Api Peut Sague terletak di Kab\\Kota Pidie Meriah, Daerah Istimewa Aceh dengan posisi geografis di Latitude 4.914°LU, Longitude 96.329°BT dan memiliki ketinggian 2801 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/PEU/PEU202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Asap kawah nihil. Cuaca cerah hingga hujan, angin lemah hingga sedang ke arah utara dan selatan.",
            "other_description":"Carrier off",
            "climatology":"KlimatologiCuaca cerah hingga hujan, angin lemah hingga sedang ke arah utara dan selatan. Suhu udara sekitar 22-30°C.",
            "seismic_observation":"Pengamatan KegempaanNihil",
            "recommendation":"RekomendasiMasyarakat/pendaki G. Peut Sague tidak diperbolehkan memasuki area kawah aktif dan tidak diperbolehkan bermalam disekitar kawah."
         }
      },
      "Rokatenda":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214116?signature=6776a67eb8f777f45213a1b03d04515cbc24cf2d9f2d04aa8cc0f483e20f55e7",
         "detail":{
            "title":"Rokatenda, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Diyan Muharomidin",
            "location":"Gunung Api Rokatenda terletak di Kab\\Kota Sikka, Nusa Tenggara Timur dengan posisi geografis di Latitude -8.32°LU, Longitude 121.708°BT dan memiliki ketinggian 875 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/ROK/ROK202302022400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-I hingga tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca berawan hingga hujan, angin lemah ke arah timur dan selatan.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah ke arah timur dan selatan.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Vulkanik Dangkal dengan amplitudo 26 mm, dan lama gempa 10 detik.2 kali gempa Tektonik Lokal dengan amplitudo 2-5 mm, S-P 2-6 detik dan lama gempa 15-37 detik.1 kali gempa Tektonik Jauh dengan amplitudo 3 mm, S-P 17 detik dan lama gempa 76 detik.",
            "recommendation":"Rekomendasi1. Masyarakat disekitar G. Rokatenda dan wisatawan dihimbau agar tidak melakukan kegiatan di sekitar kawah G . Rokatenda untuk menghindari ancaman gas beracun  maupun disekitar lembah/sungai yang berhulu di G. Rokatenda untuk menghindari banjir lahar akibat hujan.2. Masyarakat agar senantiasa mengikuti arahan pemerintah daerah setempat serta tidak mempercayai isu-isu mengenai aktivitas G. Rokatenda yang tidak jelas sumbernya.3. Pusat Vulkanologi dan Mitigasi Bencana Geologi, Badan Geologi akan selalu berkoordinasi dengan BNPB, pemerintah setempat, BPBD provinsi Nusa Tenggara Timur dan BPBD Kab Sikka dalam memberikan informasi tentang aktivitas G. Rokatenda.4. Masyarakat maupun BNPB, BPBD,  provinsi Nusa Tenggara Timur, BPBD Kab Sikka dan instansi terkait lainnya dapat memantau perkembangan tingkat aktivitas maupun rekomendasi G. Rokatenda setiap saat melalui Magma Indonesia yang dapat diakses melalui website https://magma.esdm.go.id atau apps di Android Magma Indonesia yang dapat diunduh di Google Play Store."
         }
      },
      "Ruang":{
         "location":"Sulawesi Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214106?signature=65ed78c89255d92242a542f132d72e67bc99c0510912d28896882ce4e4248fc1",
         "detail":{
            "title":"Ruang, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Julius Rampolii",
            "location":"Gunung Api Ruang terletak di Kab\\Kota Siau Tagulandang Biaro (Sitaro), Sulawesi Utara dengan posisi geografis di Latitude 2.3031°LU, Longitude 125.3667°BT dan memiliki ketinggian 725 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/RUA/RUA202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-I. Asap kawah nihil. Cuaca cerah hingga hujan, angin lemah hingga sedang ke arah timur.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca cerah hingga hujan, angin lemah hingga sedang ke arah timur. Suhu udara sekitar 27-32°C. Intensitas curah hujan 3 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan12 kali gempa Tektonik Jauh dengan amplitudo 4-33 mm, S-P 12-40 detik dan lama gempa 35-130 detik.",
            "recommendation":"Rekomendasi(1) Masyarakat dan pengunjung/wisatawan agar membatasi aktivitas (tidak berlama-lama) dan tidak bermalam di daerah kawah aktif, serta tidak mendekati lubang tembusan gas yang berada di sekitar kawah untuk menghindari potensi bahaya gas beracun."
         }
      },
      "Salak":{
         "location":"Jawa Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214093?signature=9b6e319399f7d3703c778ee592b4af633ba11d002140e8a03e7f09dfdeb98081",
         "detail":{
            "title":"Salak, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Yudha Pratama",
            "location":"Gunung Api Salak terletak di Kab\\Kota Sukabumi, Bogor, Jawa Barat dengan posisi geografis di Latitude -6.72°LU, Longitude 106.73°BT dan memiliki ketinggian 2211 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/SAL/SAL202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca cerah hingga mendung, angin lemah ke arah selatan.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca cerah hingga mendung, angin lemah ke arah selatan. Suhu udara sekitar 22-28°C.",
            "seismic_observation":"Pengamatan Kegempaan3 kali gempa Tektonik Jauh dengan amplitudo 10-20 mm, S-P 11-13 detik dan lama gempa 61-129 detik.",
            "recommendation":"RekomendasiMasyarakat disekitaran Gunungapi Salak dan para pengunjung/wisatawan, tidak diperbolehkan mendekati Kawah (Kawah Ratu, Kawah Hirup, Kawah Paeh), apalagi di musim hujan."
         }
      },
      "Seulawah Agam":{
         "location":"Daerah Istimewa Aceh",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214139?signature=ba6cb2070c44be5f8da73f3a01b8196b1745d80692c0d2c5008d6ed496a59b63",
         "detail":{
            "title":"Seulawah Agam, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Indra Syahputra",
            "location":"Gunung Api Seulawah Agam terletak di Kab\\Kota Aceh Besar, Daerah Istimewa Aceh dengan posisi geografis di Latitude 5.448°LU, Longitude 95.658°BT dan memiliki ketinggian 1810 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/SEU/SEU202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Asap kawah nihil. Cuaca cerah hingga mendung, angin lemah hingga sedang ke arah timur dan barat.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca cerah hingga mendung, angin lemah hingga sedang ke arah timur dan barat. Suhu udara sekitar 24-33°C.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Tektonik Jauh dengan amplitudo 8 mm, S-P tidak teramati dan lama gempa 90 detik.",
            "recommendation":"RekomendasiMasyarakat dan pengunjung tidak diperbolehkan masuk ke kawasan solfatara dan bermalam disekitar kawah karena konsentrasi gas vulkanik dapat membahayakan kehidupan."
         }
      },
      "Sirung":{
         "location":"Nusa Tenggara Timur",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214145?signature=d25ee9451a8fdb28382765bd87eefa75e6f14e22948565a23e47ec4966c2d5a5",
         "detail":{
            "title":"Sirung, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Fransiskus Desales Molo",
            "location":"Gunung Api Sirung terletak di Kab\\Kota Alor, Nusa Tenggara Timur dengan posisi geografis di Latitude -8.508°LU, Longitude 124.13°BT dan memiliki ketinggian 862 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/SIR/SIR202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-I. Asap kawah nihil. Cuaca berawan hingga hujan, angin lemah ke arah timur laut dan timur.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah ke arah timur laut dan timur. Suhu udara sekitar 27-30°C. Intensitas curah hujan 5 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan4 kali gempa Hembusan dengan amplitudo 1-2 mm, dan lama gempa 5-20 detik.1 kali gempa Tektonik Jauh dengan amplitudo 7 mm, S-P 12.5 detik dan lama gempa 90 detik.",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Sirung maupun pengunjung/wisatawan agar membatasi aktivitas dan tidak berlama-lama berada disekitar kawah, tidak mendekati danau kawah yang bersifat asam, tidak bermalam diarea kawah aktif dan tidak mendekati lubang tembusan gas untuk menghindari potensi bahaya gas beracun."
         }
      },
      "Slamet":{
         "location":"Jawa Tengah",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214081?signature=011eda7c455708aa64b2bd9753b38502fe1741b0f85c602f3d56bf967ab2684f",
         "detail":{
            "title":"Slamet, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Muhammad Rusdi",
            "location":"Gunung Api Slamet terletak di Kab\\Kota Pemalang, Banyumas, Brebes, Tegal, Purbalingga, Jawa Tengah dengan posisi geografis di Latitude -7.242°LU, Longitude 109.208°BT dan memiliki ketinggian 3428 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/SLA/SLA202302022400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-I hingga tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca berawan hingga hujan, angin lemah ke arah selatan.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah ke arah selatan. Suhu udara sekitar 21-26.7°C. Kelembaban 72-90%.",
            "seismic_observation":"Pengamatan Kegempaan58 kali gempa Hembusan dengan amplitudo 3-7 mm, dan lama gempa 8-33 detik.1 kali gempa Tektonik Lokal dengan amplitudo 28 mm, S-P 5.3 detik dan lama gempa 24 detik.1 kali gempa Tektonik Jauh dengan amplitudo 9 mm, S-P 21.5 detik dan lama gempa 59 detik.1 kali gempa Tremor Menerus dengan amplitudo 0.5-2 mm, dominan 0.5 mm.",
            "recommendation":"RekomendasiMasyarakat dan pengunjungh/wisatawan tidak berada/beraktivitas dalam radius 1km dari kawah puncak G. Slamet."
         }
      },
      "Sorikmarapi":{
         "location":"Sumatera Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214110?signature=4cafad392837db407f9e8b4e302e4787725b25d2289e2ff443a47b892945723b",
         "detail":{
            "title":"Sorikmarapi, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Kisroh",
            "location":"Gunung Api Sorikmarapi terletak di Kab\\Kota Mandailing Natal, Sumatera Utara dengan posisi geografis di Latitude 0.686°LU, Longitude 99.537°BT dan memiliki ketinggian 2145 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/SOR/SOR202302022400.png",
            "visual_observation":"Gunung api terlihat jelas. Teramati asap kawah utama berwarna putih dengan intensitas tipis tinggi sekitar 30-40 meter dari puncak. Cuaca cerah hingga berawan, angin lemah hingga sedang ke arah selatan.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca cerah hingga berawan, angin lemah hingga sedang ke arah selatan. Suhu udara sekitar 21-28°C.",
            "seismic_observation":"Pengamatan KegempaanNihil",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Sorik Marapi dan pengunjung/wisatawan(a) tidak diperbolehkan mendekati kawah dalam jarak dekat(b) segera menjauhi/meninggalkan area sekitar kawah jika teramati peningkatan intensitas/ketebalan asap kawah dan/atau jika tercium bau gas yang menyengat untuk menghindari potensi bahaya paparan gas beracun maupun erupsi freatik."
         }
      },
      "Sumbing":{
         "location":"Jawa Tengah",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214137?signature=e2bf32b5c31e5b377a7d9621606a2f09c6dcaa24e10a565d3c885fdc27ad88d0",
         "detail":{
            "title":"Sumbing, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Warseno",
            "location":"Gunung Api Sumbing terletak di Kab\\Kota Magelang, Temanggung, Wonosobo, Jawa Tengah dengan posisi geografis di Latitude -7.384°LU, Longitude 110.07°BT dan memiliki ketinggian 3371 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/SBG/SBG202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Asap kawah nihil. Cuaca cerah hingga hujan, angin lemah ke arah timur laut, timur dan barat laut.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca cerah hingga hujan, angin lemah ke arah timur laut, timur dan barat laut. Suhu udara sekitar 18.5-24.7°C. Kelembaban 100%. Tekanan udara 674.7-675.8 mmHg. Intensitas curah hujan 0.8 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan1 kali gempa Tektonik Lokal dengan amplitudo 13.57 mm, S-P 5.66 detik dan lama gempa 12.46 detik.4 kali gempa Tektonik Jauh dengan amplitudo 13.18-71.14 mm, S-P 31.91 detik dan lama gempa 69.83-152.34 detik.",
            "recommendation":"RekomendasiPengunjung/wisatawan agar berhati-hati ketika berada di lokasi kawah karena struktur batunya labil dan mudah lepas serta tidak berkemah di dasar kawah karena dimungkinkan terdapat gas vulkanik beracun pada malam hari terutama pada saat cuaca buruk."
         }
      },
      "Sundoro":{
         "location":"Jawa Tengah",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214123?signature=7ed7253a37f3687fa1c4a9de7f9082efa51cdf2f42507a15cb03422c04d701df",
         "detail":{
            "title":"Sundoro, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Maryani",
            "location":"Gunung Api Sundoro terletak di Kab\\Kota Temanggung, Wonosobo, Jawa Tengah dengan posisi geografis di Latitude -7.3°LU, Longitude 109.992°BT dan memiliki ketinggian 3160 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/SUN/SUN202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Asap kawah nihil. Cuaca cerah hingga hujan, angin lemah ke arah timur laut, timur dan barat laut.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca cerah hingga hujan, angin lemah ke arah timur laut, timur dan barat laut. Suhu udara sekitar 18.5-24.7°C. Kelembaban 100%. Tekanan udara 674.7-675.8 mmHg. Intensitas curah hujan 0.8 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan3 kali gempa Tektonik Lokal dengan amplitudo 2.97-12.29 mm, S-P 4.68-6.28 detik dan lama gempa 13.31-25.63 detik.4 kali gempa Tektonik Jauh dengan amplitudo 3.02-15.92 mm, S-P 26.18-27.57 detik dan lama gempa 78.57-134.63 detik.",
            "recommendation":"Rekomendasi1). Masyarakat disekitar agar tenang, tidak terpancing isyu-isyu tentang letusan G.Sundoro.2). Masyarakat disekitar Gunungapi Sundoro dan pengunjung/wisatawan tidak diperbolehkan mendekati bibir kawah puncak G.Sundoro dalam radius 200 meter.3). Masyarakat yang bertempat tinggal di sekitar Gunungapi Sundoro dalam KRB II bisa beraktivitas seperti biasa dan tetap memperhatikan perkembangan kegiatan G.Sundoro yang dikeluarkan oleh BPBD setempat.4). Pusat Vulkanologi dan Mitigasi Bencana Geologi selalu berkoordinasi dengan Pemerintah Jawa Tengah dan BPBD kabupaten Temanggung, BPBD kabupaten Wonosobo tentang aktivitas G.Sundoro, Masyarakat agar selalu mengikuti arahan dari BPBD setempat.5). Agar BPBD kabupaten Temanggung, kabupaten Wonosobo senantiasa berkoordinasi dengan pos pengamatan Gunungapi Sundoro dan Sumbing di Desa Gentingsari Kecamatan Bansari kabupaten Temanggung atau dengan Pusat Vulkanologi dan Mitigasi Bencana Geologi di Bandung."
         }
      },
      "Talang":{
         "location":"Sumatera Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214102?signature=0762bfdaa71b4037917ff1567b03382ca5bd1cb4f5413c7d2b49b31b584df7dd",
         "detail":{
            "title":"Talang, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Yuda Prinardita Pura",
            "location":"Gunung Api Talang terletak di Kab\\Kota Solok, Sumatera Barat dengan posisi geografis di Latitude -0.978°LU, Longitude 100.679°BT dan memiliki ketinggian 2597 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/TAL/TAL202302022400.png",
            "visual_observation":"Gunung api terlihat jelas. Teramati asap kawah utama berwarna putih dengan intensitas tipis tinggi sekitar 25 meter dari puncak. Cuaca berawan, angin lemah ke arah timur.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan, angin lemah ke arah timur. Suhu udara sekitar 20-29.5°C.",
            "seismic_observation":"Pengamatan KegempaanNihil",
            "recommendation":"RekomendasiMasyarakat disekitar Gunungapi Talang dan pengunjung/wisatawan tidak diperbolehkan mendekati kawah utama dan kawah selatan dalam jarak dekat"
         }
      },
      "Tambora":{
         "location":"Nusa Tenggara Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214127?signature=9dbc35213abf4260be07ca8c7d0aad103a36b480be156c61a8bef14df8e5338a",
         "detail":{
            "title":"Tambora, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Rasyidin",
            "location":"Gunung Api Tambora terletak di Kab\\Kota Dompu, Bima, Nusa Tenggara Barat dengan posisi geografis di Latitude -8.25°LU, Longitude 118°BT dan memiliki ketinggian 2850 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/TAM/TAM202302022400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-I hingga tertutup Kabut 0-III. Asap kawah tidak teramati. Cuaca berawan hingga hujan, angin lemah hingga sedang ke arah selatan.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah hingga sedang ke arah selatan. Suhu udara sekitar 23-32°C. Kelembaban 65-95%. Intensitas curah hujan 72 mm per hari.",
            "seismic_observation":"Pengamatan Kegempaan2 kali gempa Hembusan dengan amplitudo 12-20 mm, dan lama gempa 62-73 detik.12 kali gempa Vulkanik Dalam dengan amplitudo 6-34 mm, S-P 0.5-2 detik dan lama gempa 7-15 detik.4 kali gempa Tektonik Lokal dengan amplitudo 28-64 mm, S-P 4-6 detik dan lama gempa 40-65 detik.",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Tambora dan pengunjung/wisatawan agar tidak mendekati Kubah Lava Doro Afi Toi maupun Doro Afi Bou dan tidak mendekati lubang tembusan gas yang berada di dasar kaldera Tambora, serta membatasi aktivitas (tidak berlama-lama berada) di sekitar pusat aktivitas."
         }
      },
      "Tandikat":{
         "location":"Sumatera Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214103?signature=220f5935487f3739dbc7938c28d4ac481da60d6e1c107acefd65de30b0a487dc",
         "detail":{
            "title":"Tandikat, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Musmulyadi",
            "location":"Gunung Api Tandikat terletak di Kab\\Kota Padang Pariaman, Agam, Sumatera Barat dengan posisi geografis di Latitude -0.39°LU, Longitude 100.331°BT dan memiliki ketinggian 2438 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/TAN/TAN202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Asap kawah nihil. Cuaca cerah hingga mendung, angin lemah ke arah timur.",
            "other_description":"Nihil",
            "climatology":"KlimatologiCuaca cerah hingga mendung, angin lemah ke arah timur. Suhu udara sekitar 20-24°C. Kelembaban 55-60%.",
            "seismic_observation":"Pengamatan Kegempaan2 kali gempa Tektonik Lokal dengan amplitudo 27-31 mm, S-P 3.5 detik dan lama gempa 34-35 detik.1 kali gempa Tektonik Jauh dengan amplitudo 1 mm, S-P tidak teramati dan lama gempa 165 detik.",
            "recommendation":"RekomendasiPengunjung/wisatawan agar berhati-hati ketika berada di lokasi kawah karena struktur batunya labil dan mudah lepas serta tidak berkemah di dasar kawah karena dimungkinkan terdapat gas vulkanik beracun pada malam hari terutama pada saat cuaca buruk."
         }
      },
      "Tangkoko":{
         "location":"Sulawesi Utara",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214109?signature=40598c02bf3d13c9fd9916f259595f5e8fe5a7ee3eba8edc7b427284ab109166",
         "detail":{
            "title":"Tangkoko, Kamis - 02 Februari 2023, periode 00:00-24:00 WITA",
            "author":" Yappie Fredrik Albert Rombot",
            "location":"Gunung Api Tangkoko terletak di Kab\\Kota Bitung, Sulawesi Utara dengan posisi geografis di Latitude 1.518°LU, Longitude 125.185°BT dan memiliki ketinggian 1334 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/TGK/TGK202302022400.png",
            "visual_observation":"Gunung api tertutup Kabut 0-I hingga tertutup Kabut 0-II. Asap kawah nihil. Cuaca berawan hingga hujan, angin lemah hingga sedang ke arah utara.",
            "other_description":"Peralatan seismik pos Tangkoko mengalami masalah pada motor penggerak Drum dan dalam Perbaikan",
            "climatology":"KlimatologiCuaca berawan hingga hujan, angin lemah hingga sedang ke arah utara. Suhu udara sekitar 21-30°C.",
            "seismic_observation":"Pengamatan Kegempaan2 kali gempa Tektonik Jauh dengan amplitudo 30-54 mm, S-P 14-17 detik dan lama gempa 45-65 detik.",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Tangkoko dan pengunjung/wisatawan agar membatasi aktivitas (tidak berlama-lama) dan tidak bermalam di area kawah aktif,serta tidak mendekati lubang tembusan gas yang berada di sekitar kawah untuk menghindari potensi bahaya gas beracun."
         }
      },
      "Tangkuban Parahu":{
         "location":"Jawa Barat",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214125?signature=5d7cee319d0b8863fcee3fe17cd12a7fca22936010b389729271d30150aa4efc",
         "detail":{
            "title":"Tangkuban Parahu, Kamis - 02 Februari 2023, periode 00:00-24:00 WIB",
            "author":" Ilham Mardikayanta",
            "location":"Gunung Api Tangkuban Parahu terletak di Kab\\Kota Subang, Bandung, Jawa Barat dengan posisi geografis di Latitude -6.77°LU, Longitude 107.6°BT dan memiliki ketinggian 2084 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/TPR/TPR202302022400.png",
            "visual_observation":"Gunung api terlihat jelas hingga tertutup Kabut 0-III. Teramati asap kawah utama berwarna putih dengan intensitas tipis, sedang hingga tebal tinggi asap tidak teramati. Cuaca cerah hingga mendung, angin lemah hingga kencang ke arah utara dan selatan.",
            "other_description":"Tekanan gas kawah Ecoma sedang-kuat, dihimbau kepada pengelola wisata, para pedagang, pengunjung untuk tetap berhati-hati",
            "climatology":"KlimatologiCuaca cerah hingga mendung, angin lemah hingga kencang ke arah utara dan selatan. Suhu udara sekitar 17-22°C.",
            "seismic_observation":"Pengamatan Kegempaan9 kali gempa Low Frequency dengan amplitudo 2-12 mm, dan lama gempa 10-21 detik.3 kali gempa Tektonik Jauh dengan amplitudo 2.5-28 mm, S-P 22 detik dan lama gempa 75-135 detik.",
            "recommendation":"Rekomendasi1. (a) Masyarakat di sekitar G. Tangkuban Parahu, pedagang, wisatawan, dan pendaki tidak turun ke dasar Kawah Ratu dan Kawah Upas, serta tidak diperbolehkan menginap/berlama-lama berada di dalam kawasan kawah-kawah aktif yang ada di dalam kompleks G. Tangkuban Parahu. (b) Segera menjauhi/meninggalkan area sekitar kawah jika teramati peningkatan intensitas/ketebalan asap kawah dan/atau jika tercium bau gas yang menyengat untuk menghindari potensi bahaya paparan gas beracun maupun erupsi freatik.2. Mewaspadai meningkatnya konsentrasi gas-gas vulkanik yang dapat terjadi secara tiba-tiba, yaitu dengan tidak berlama-lama berada di sekitar area kawah aktif G. Tangkuban Parahu agar terhindar dari paparan gas yang dapat berdampak bagi kesehatan dan keselamatan jiwa.3. Mewaspadai terjadinya letusan freatik yang dapat terjadi secara tiba-tiba dan tanpa didahului oleh gejala peningkatan vulkanik yang jelas.4. Masyarakat di sekitar G. Tangkuban Parahu diharap tenang, beraktivitas seperti biasa, tidak terpancing isu-isu tentang letusan G. Tangkuban Parahu, tetap memperhatikan perkembangan kegiatan G. Tangkuban Parahu yang dikeluarkan oleh BPBD setempat dan selalu mengikuti arahan dari BPBD setempat."
         }
      },
      "Wurlali":{
         "location":"Maluku",
         "link":"https://magma.esdm.go.id/v1/gunung-api/laporan/214118?signature=c38255516d8089729183534bf2ef40d97bdd80e7885a7563b2ab83af297e58ff",
         "detail":{
            "title":"Wurlali, Kamis - 02 Februari 2023, periode 00:00-24:00 WIT",
            "author":" Marinus A. Louth",
            "location":"Gunung Api Wurlali terletak di Kab\\Kota Maluku Barat Daya, Maluku dengan posisi geografis di Latitude -7.125°LU, Longitude 128.675°BT dan memiliki ketinggian 868 mdpl",
            "image":"https://magma.vsi.esdm.go.id/img/ga/WUR/WUR202302022400.png",
            "visual_observation":"Gunung api terlihat jelas. Teramati asap kawah utama berwarna putih dengan intensitas sedang tinggi sekitar 100 meter dari puncak. Cuaca cerah hingga berawan, angin sedang ke arah barat.",
            "other_description":"Seismik nihil",
            "climatology":"KlimatologiCuaca cerah hingga berawan, angin sedang ke arah barat.",
            "seismic_observation":"Pengamatan KegempaanNihil",
            "recommendation":"RekomendasiMasyarakat di sekitar G. Wurlali dan pengunjung/wisatawan agar membatasi aktivitas (tidak berlama-lama) dan tidak bermalam di area kawah aktif, serta tidak mendekati lubang tembusan gas yang berada di sekitar kawah untuk menghindari potensi bahaya gas beracun."
         }
      }
   }
}
```
