# Hidra
Hidra is used to forward the packets of the SA:MP Query, in a few words clone the Query of some server to show them on yours.

## Example
```python
fake_server = CloneQuery('127.0.0.1', 7777, '51.75.33.152', 7777)
fake_server.start()
```
### Result
![](https://i.imgur.com/HdvoC1u.png)

![](https://i.imgur.com/B5v2SCC.png)

## Features
* Multi-Threading
* Clone multiple servers in the same script (Object based)

## Functions
`refresh` - Update the query info

`start` - Init listening

`stop` - Stop listening
