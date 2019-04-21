lives = memory.readbyte(0x0736)
prev_live = lives

function update_lives()
	lives = memory.readbyte(0x0736)
	return compare(lives)
end

function compare(lives)
	if lives < prev_live then
		prev_live = lives
		--print("you died")
		file1 = io.open("boolean.txt", "w+")
		file1:write("True\n")
		file1:close()
		
	elseif lives > prev_live then
		prev_live = lives
		--print("you gained lives")
	end
end

while (true) do
	memory.register(0x0736, update_lives)
    emu.frameadvance()
end

    
	