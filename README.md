# vscode-go-snippets
VS Code Go extension predefined snippets for quick coding

`im`: Snippet for import statement
```go
import "${1:package}"
```

`ims`: Snippet for a import block
```go
import (
	"${1:package}"
)
```

`co`: Snippet for a constant
```go
const ${1:name} = ${2:value}
```

`cos`: Snippet for a constant block
```go
const (
	${1:name} = ${2:value}
)
```

`tyf`: Snippet for a type function declaration
```go
type ${1:name} func($3) $4
```

`tyi`: Snippet for a type interface
```go
type ${1:name} interface {
	$0
}
```

`tys`: Snippet for a struct declaration
```go
type ${1:name} struct {
	$0
}
```

`pkgm`: Snippet for main package & function
```go
package main

func main() {
	$0
}
```

`func`: Snippet for function declaration
```go
func $1($2) $3 {
	$0
}
```

`var`: Snippet for a variable
```go
var ${1:name} ${2:type}
```

`switch`: Snippet for switch statement
```go
switch ${1:expression} {
case ${2:condition}:
	$0
}
```

`sel`: Snippet for select statement
```go
select {
case ${1:condition}:
	$0
}
```

`cs`: Snippet for case clause
```go
case ${1:condition}:$0
```

`for`: Snippet for a for loop
```go
for ${1:i} := ${2:0}; $1 < ${3:count}; $1${4:++} {
	$0
}
```

`forr`: Snippet for a for range loop
```go
for ${1:_, }${2:v} := range ${3:v} {
	$0
}
```

`ch`: Snippet for a channel
```go
chan ${1:type}
```

`map`: Snippet for a map
```go
map[${1:type}]${2:type}
```

`in`: Snippet for empty interface
```go
interface{}
```

`if`: Snippet for if statement
```go
if ${1:condition} {
	$0
}
```

`el`: Snippet for else branch
```go
else {
	$0
}
```

`ie`: Snippet for if else
```go
if ${1:condition} {
	$2
} else {
	$0
}
```

`iferr`: Snippet for if err != nil
```go
if err != nil {
	${1:return ${2:nil, }${3:err}}
}
```

`fp`: Snippet for fmt.Println()
```go
fmt.Println("$1")
```

`ff`: Snippet for fmt.Printf()
```go
fmt.Printf("$1", ${2:var})
```

`lp`: Snippet for log.Println()
```go
log.Println("$1")
```

`lf`: Snippet for log.Printf()
```go
log.Printf("$1", ${2:var})
```

`lv`: Snippet for log.Printf() with variable content
```go
log.Printf("${1:var}: %#+v\\n", ${1:var})
```

`tl`: Snippet for t.Log()
```go
t.Log("$1")
```

`tlf`: Snippet for t.Logf()
```go
t.Logf("$1", ${2:var})
```

`tlv`: Snippet for t.Logf() with variable content
```go
t.Logf("${1:var}: %#+v\\n", ${1:var})
```

`make`: Snippet for make statement
```go
make(${1:type}, ${2:0})
```

`new`: Snippet for new statement
```go
new(${1:type})
```

`pn`: Snippet for panic
```go
panic("$0")
```

`wr`: Snippet for http Response
```go
${1:w} http.ResponseWriter, ${2:r} *http.Request
```

`hf`: Snippet for http.HandleFunc()
```go
${1:http}.HandleFunc("${2:/}", ${3:handler})
```

`hand`: Snippet for http handler declaration
```go
func $1(${2:w} http.ResponseWriter, ${3:r} *http.Request) {
	$0
}
```

`rd`: Snippet for http.Redirect()
```go
http.Redirect(${1:w}, ${2:r}, "${3:/}", ${4:http.StatusFound})
```

`herr`: Snippet for http.Error()
```go
http.Error(${1:w}, ${2:err}.Error(), ${3:http.StatusInternalServerError})
```

`las`: Snippet for http.ListenAndServe
```go
http.ListenAndServe("${1::8080}", ${2:nil})
```

`sv`: Snippet for http.Serve
```go
http.Serve("${1::8080}", ${2:nil})
```

`go`: Snippet for anonymous goroutine declaration
```go
go func($1) {
	$0
}($2)
```

`gf`: Snippet for goroutine declaration
```go
go ${1:func}($0)
```

`df`: Snippet for defer statement
```go
defer ${1:func}($0)
```

`tf`: Snippet for Test function
```go
func Test$1(t *testing.T) {
	$0
}
```

`tm`: Snippet for TestMain function
```go
func TestMain(m *testing.M) {
	$1

	os.Exit(m.Run())
}
```

`bf`: Snippet for Benchmark function
```go
func Benchmark$1(b *testing.B) {
	for ${2:i} := 0; ${2:i} < b.N; ${2:i}++ {
		$0
	}
}
```

`ef`: Snippet for Example function
```go
func Example$1() {
	$2
	//Output:
	$3
}
```

`tdt`: Snippet for table driven test
```go
func Test$1(t *testing.T) {
	testCases := []struct {
		desc	string
		$2
	}{
		{
			desc: "$3",
			$4
		},
	}
	for _, tC := range testCases {
		t.Run(tC.desc, func(t *testing.T) {
			$0
		})
	}
}
```

`finit`: Snippet for init function
```go
func init() {
	$1
}
```

`fmain`: Snippet for main function
```go
func main() {
	$1
}
```

`meth`: Snippet for method declaration
```go
func (${1:receiver} ${2:type}) ${3:method}($4) $5 {
	$0
}
```

`helloweb`: Snippet for sample hello world webapp
```go
package main

import (
	"fmt"
	"net/http"
	"time"
)

func greet(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello World! %s", time.Now())
}

func main() {
	http.HandleFunc("/", greet)
	http.ListenAndServe(":8080", nil)
}
```

`sort`: Snippet for a custom sort.Sort interface implementation, for a given slice type.
```go
type ${1:SortBy} []${2:Type}

func (a $1) Len() int           { return len(a) }
func (a $1) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a $1) Less(i, j int) bool { ${3:return a[i] < a[j]} }
```
