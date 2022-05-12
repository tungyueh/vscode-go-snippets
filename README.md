# vscode-go-snippets
VS Code Go extension predefined snippets for quick coding

Make https://github.com/golang/vscode-go/blob/master/snippets/go.json more readable

`im`: Snippet for import statement
```go
import "package"
```

`ims`: Snippet for a import block
```go
import (
	"package"
)
```

`co`: Snippet for a constant
```go
const name = value
```

`cos`: Snippet for a constant block
```go
const (
	name = value
)
```

`tyf`: Snippet for a type function declaration
```go
type name func() 
```

`tyi`: Snippet for a type interface
```go
type name interface {
	
}
```

`tys`: Snippet for a struct declaration
```go
type name struct {
	
}
```

`pkgm`: Snippet for main package & function
```go
package main

func main() {
	
}
```

`func`: Snippet for function declaration
```go
func ()  {
	
}
```

`var`: Snippet for a variable
```go
var name type
```

`switch`: Snippet for switch statement
```go
switch expression {
case condition:
	
}
```

`sel`: Snippet for select statement
```go
select {
case condition:
	
}
```

`cs`: Snippet for case clause
```go
case condition:
```

`for`: Snippet for a for loop
```go
for i := 0; i < count; i++ {
	
}
```

`forr`: Snippet for a for range loop
```go
for _, v := range v {
	
}
```

`ch`: Snippet for a channel
```go
chan type
```

`map`: Snippet for a map
```go
map[type]type
```

`in`: Snippet for empty interface
```go
interface{}
```

`if`: Snippet for if statement
```go
if condition {
	
}
```

`el`: Snippet for else branch
```go
else {
	
}
```

`ie`: Snippet for if else
```go
if condition {
	
} else {
	
}
```

`iferr`: Snippet for if err != nil
```go
if err != nil {
	return nil, err
}
```

`fp`: Snippet for fmt.Println()
```go
fmt.Println("")
```

`ff`: Snippet for fmt.Printf()
```go
fmt.Printf("", var)
```

`lp`: Snippet for log.Println()
```go
log.Println("")
```

`lf`: Snippet for log.Printf()
```go
log.Printf("", var)
```

`lv`: Snippet for log.Printf() with variable content
```go
log.Printf("var: %#+v\\n", var)
```

`tl`: Snippet for t.Log()
```go
t.Log("")
```

`tlf`: Snippet for t.Logf()
```go
t.Logf("", var)
```

`tlv`: Snippet for t.Logf() with variable content
```go
t.Logf("var: %#+v\\n", var)
```

`make`: Snippet for make statement
```go
make(type, 0)
```

`new`: Snippet for new statement
```go
new(type)
```

`pn`: Snippet for panic
```go
panic("")
```

`wr`: Snippet for http Response
```go
w http.ResponseWriter, r *http.Request
```

`hf`: Snippet for http.HandleFunc()
```go
http.HandleFunc("/", handler)
```

`hand`: Snippet for http handler declaration
```go
func (w http.ResponseWriter, r *http.Request) {
	
}
```

`rd`: Snippet for http.Redirect()
```go
http.Redirect(w, r, "/", http.StatusFound)
```

`herr`: Snippet for http.Error()
```go
http.Error(w, err.Error(), http.StatusInternalServerError)
```

`las`: Snippet for http.ListenAndServe
```go
http.ListenAndServe(":8080", nil)
```

`sv`: Snippet for http.Serve
```go
http.Serve(":8080", nil)
```

`go`: Snippet for anonymous goroutine declaration
```go
go func() {
	
}()
```

`gf`: Snippet for goroutine declaration
```go
go func()
```

`df`: Snippet for defer statement
```go
defer func()
```

`tf`: Snippet for Test function
```go
func Test(t *testing.T) {
	
}
```

`tm`: Snippet for TestMain function
```go
func TestMain(m *testing.M) {
	

	os.Exit(m.Run())
}
```

`bf`: Snippet for Benchmark function
```go
func Benchmark(b *testing.B) {
	for i := 0; i < b.N; i++ {
		
	}
}
```

`ef`: Snippet for Example function
```go
func Example() {
	
	//Output:
	
}
```

`tdt`: Snippet for table driven test
```go
func Test(t *testing.T) {
	testCases := []struct {
		desc	string
		
	}{
		{
			desc: "",
			
		},
	}
	for _, tC := range testCases {
		t.Run(tC.desc, func(t *testing.T) {
			
		})
	}
}
```

`finit`: Snippet for init function
```go
func init() {
	
}
```

`fmain`: Snippet for main function
```go
func main() {
	
}
```

`meth`: Snippet for method declaration
```go
func (receiver type) method()  {
	
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
type SortBy []Type

func (a SortBy) Len() int           { return len(a) }
func (a SortBy) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a SortBy) Less(i, j int) bool { return a[i] < a[j] }
```
