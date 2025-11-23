set ignorecase                  "검색시 대소문자 구별하지 않음(= set ic)
set hlsearch                    "검색된 문자열을 강조
set incsearch                   "검색어를 입력할 때마다 일치하는 문자열을 강조(= set is)
set expandtab                   "tab 대신 띄어쓰기로 (=set et)
set background=dark             "배경을 어둡게
set nocompatible                "방향키로 이동 가능하게
set fileencodings=utf-8,euc-kr  "인코딩 설정
set fencs=ucs-bom,utf-8,euc-kr  "한글 파일은 euc-kr, 유니코드는 유니코드
set bs=indent,eol,start         "backspace 키 사용 가능하게
set history=1000                "명령어에 대한 히스토리를 1000개까지 저장
set showmatch                   "매칭되는 괄호를 표시
set nowrap                      "자동 줄바꿈 하지 않음
set wmnu                        "tab 자동 완성시 가능한 목록을 표시
set nobackup                    "백업파일을 만들지 않음
set autoindent                  "자동 들여쓰기 (= set ai)
set smartindent                 "스마트 들여쓰기 (= set si)
set tabstop=4                   "탭크기를 4로 변경(기본은 8)
set shiftwidth=4                ">>, << 를 눌렀을 때 커서 너비=4
set number                      "줄번호 표시 (= set nu)
set cursorline                  "커서있는 행 밑줄
set ruler                       "커서 좌표 표시
set cindent                     "C언어를 위한 들여쓰기
set title                       "현재 편집중인 파일 이름 표시
set mouse=a                     "커서 이동을 마우스로 가능하도록

syntax on                       "문법기능 On
filetype plugin indent on       "확장자로 문서형식 파악